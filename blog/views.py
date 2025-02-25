from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from blog.models import post



def blog_page(request):
    posts = post.objects.filter(publish_date__lte=timezone.now(),status=True)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)
def single_page(request,pid):
    Posts = post.objects.filter(status=1)
    Post = get_object_or_404(Posts , pk=pid)
    Post.counted_views+=1
    Post.save()
    prev_post = post.objects.filter(status=1, id__lt=Post.id).order_by('-publish_date').first()
    next_post = post.objects.filter(status=1, id__gt=Post.id).order_by('publish_date').first()


    context = {'Post': Post ,'prev_post':prev_post , 'next_post' : next_post}
    return render(request,'blog/blog-single.html',context) 
