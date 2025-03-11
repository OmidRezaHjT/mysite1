from django import template
from blog.models import post
from django.utils import timezone

register = template.Library()
@register.inclusion_tag('website/latest_posts.html')
def latestposts():
    posts =post.objects.filter(publish_date__lte=timezone.now(),status=1)
    posts = posts.filter(status = 1).order_by('-publish_date')[:6]
    return {'posts': posts}