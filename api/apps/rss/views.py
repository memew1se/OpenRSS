import datetime

import feedparser
from adrf.views import APIView as AsyncAPIView
from django.core.cache import cache
from feedparser import FeedParserDict
from rest_framework.request import Request
from rest_framework.response import Response

from config import shared

from .models import MainFeed


class MainFeedListView(AsyncAPIView):
    async def get(self, request: Request) -> Response:
        mf = MainFeed.objects.aiterator()
        data = [
            {"id": feed.id, "slug": feed.slug, "title": feed.title, "url": feed.url}
            async for feed in mf
        ]
        return Response(data)


class MainFeedRetrieveView(AsyncAPIView):
    async def get(self, request: Request, **kwargs: dict):
        # getting parameters
        slug = kwargs["slug"]
        date = datetime.datetime.now()
        minutes_quart = date.minute // 15

        # getting cache
        feed_key = f"{slug}-{date.strftime('%d-%m-%Y-%H')}-{minutes_quart}"
        cached_rss = await cache.aget(feed_key)

        if cached_rss:
            return Response(cached_rss)
        else:
            # getting and parsing feed
            feed = await MainFeed.objects.aget(slug=slug)
            async with shared.AIOHTTP_SESSION.get(feed.url) as resp:
                text = await resp.text()
            fd: FeedParserDict = feedparser.parse(text)
            rss = {"channel": fd.channel, "entries": fd.entries}

            # setting cache
            cache_time = 15 * 60 - (date.minute % 15 * 60 + date.second)
            await cache.aset(feed_key, rss, cache_time)

            return Response(rss)
