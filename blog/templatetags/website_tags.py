from django import template
from blog.models import post
register = template.Library()
@register.inclusion_tag('website/latest_posts.html')
def latestposts():
    posts = post.objects.filter(status = 1).order_by('-publish_date')[:6]
    return {'posts': posts}