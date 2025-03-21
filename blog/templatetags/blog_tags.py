from django import template
from blog.models import post , category , Comment
register = template.Library()
@register.inclusion_tag('blog/blog-latestposts.html')
def latestposts(arg=4):
    posts = post.objects.filter(status = 1).order_by('publish_date')[:arg]
    return {'posts': posts}
@register.inclusion_tag('blog/blog-postcat.html')
def postcategories():
    posts = post.objects.filter(status = 1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories' :cat_dict}
@register.simple_tag(name='comments-count')
def function(pid):
    return Comment.objects.filter(post=pid, approach=True).order_by('-created_date').count()