from django.urls import re_path

from .views import MainFeedListView

urlpatterns = (
    re_path("^main-feed/?$", MainFeedListView.as_view(), name="rss-main-feed-list"),
)
