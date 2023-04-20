import feedparser
from adrf.views import APIView as AsyncAPIView
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
        slug = kwargs["slug"]
        feed = await MainFeed.objects.aget(slug=slug)
        async with shared.AIOHTTP_SESSION.get(feed.url) as resp:
            text = await resp.text()
        fd: FeedParserDict = feedparser.parse(text)
        rss = {"channel": fd.channel, "entries": fd.entries}

        return Response(rss)
