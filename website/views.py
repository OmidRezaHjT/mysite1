from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post

def home_page(request):
    posts = post.objects.all()
    context = {'posts':posts}
    return render(request,'website/index.html',context)
def about_page(request):
    return render(request,'website/about.html')
def contact_page(request):
    return render(request,'website/contact.html')