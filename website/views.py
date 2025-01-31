from django.shortcuts import render
from django.http import HttpResponse
def home_page(request):
    return HttpResponse('<h1>Home Page</h1>')
def about_page(request):
    return HttpResponse('<h1>hey my name is omidreza</h1>')
def contact_page(request):
    return HttpResponse('<h1>hey if u want call me this is my number 120030131</h1>')