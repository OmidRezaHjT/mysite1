from django import template
from blog.models import post
register = template.Library()
@register.template_tag(name = 'totalposts')
def function():
    posts = post.objects.filter(status = 1).count()
    return posts