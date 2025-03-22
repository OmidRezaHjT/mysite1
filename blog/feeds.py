from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import post


class LatestEntriesFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return post.objects.order_by("-pub_date")[:5]

    def item_title(self, item):
        return item.title

    def item_content(self, item):
        return item.content[:100]
