from django.shortcuts import render
from django.http import HttpResponse
def blog_page(request):
    return render(request,'blog/blog-home.html')
def single_page(request):
    return render(request,'blog/blog-single.html')
