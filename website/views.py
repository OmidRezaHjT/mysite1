from django.shortcuts import render
from django.http import HttpResponse
def home_page(request):
    return render(request,'index.html')
def about_page(request):
    return render(request,'about.html')
def contact_page(request):
    return render(request,'contact.html')