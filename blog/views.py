from django.shortcuts import render , get_object_or_404
from django.utils import timezone
from django.contrib import messages
from blog.models import post,Comment
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from blog.forms import CommentForm



def blog_page(request,cat_name=None,author_username=None,tag_name=None):
    posts = post.objects.filter(publish_date__lte=timezone.now(),status=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if tag_name:
        posts = posts.filter(tag__name__in=[tag_name])
    posts= Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request,'blog/blog-home.html', context)
def single_page(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ur comment successfully sent")
        else:
             print(form.errors)
             messages.add_message(request, messages.ERROR, "Ur comment didnt sent")

    Posts = post.objects.filter(publish_date__lte=timezone.now(),status=1)
    comments = Comment.objects.filter(post=pid,approach=True)
    form = CommentForm()
    Post = get_object_or_404(Posts , pk=pid)
    Post.counted_views+=1
    Post.save()
    comments = Comment.objects.filter(post=Post.id, approach=True).order_by('-created_date')
    prev_post = post.objects.filter(publish_date__lte=timezone.now(),status= True, id__lt=Post.id).order_by('-publish_date').first()
    next_post = post.objects.filter(publish_date__lte=timezone.now(),status= True, id__gt=Post.id).order_by('publish_date').first()
    context = {'Post': Post ,'prev_post':prev_post , 'next_post' : next_post, 'comments' : comments,'form':form}
    return render(request,'blog/blog-single.html',context) 
def blog_search(request):
    posts = post.objects.filter(publish_date__lte=timezone.now(),status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)
