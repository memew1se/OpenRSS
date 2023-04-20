from adrf.views import APIView as AsyncAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import MainFeed


class MainFeedListView(AsyncAPIView):
    async def get(self, request: Request) -> Response:
        mf = MainFeed.objects.aiterator()
        data = [
            {"id": feed.id, "slug": feed.slug, "title": feed.title, "url": feed.url}
            async for feed in mf
        ]
        return Response(data)
