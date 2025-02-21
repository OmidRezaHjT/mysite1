from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from blog.models import post



def blog_page(request):
    posts = post.objects.filter(publish_date__lte=timezone.now(),status=True)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)
def single_page(request,pid):
    Post = get_object_or_404(post , pk=pid)
    context = {'Post': Post}
    Post.counted_views+=1
    Post.save()
    return render(request,'blog/blog-single.html',context) 
