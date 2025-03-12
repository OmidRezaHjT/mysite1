from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import post
from website.forms import *

def home_page(request):
    posts = post.objects.all()
    context = {'posts':posts}
    return render(request,'website/index.html',context)
def about_page(request):
    return render(request,'website/about.html')
def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm() 
    return render(request,'website/contact.html',{'form':form})

def newsletter_page(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect("/")
