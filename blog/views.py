from django.shortcuts import render
from django.utils import timezone
from blog.models import post

def increment_post_views(post_view):
    post_view.counted_views += 1
    post_view.save()

def blog_page(request):
    posts = post.objects.filter(publish_date__lte=timezone.now())
    for p in posts:
        increment_post_views(p)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)
def single_page(request):
    return render(request,'blog/blog-single.html')
