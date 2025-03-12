from django.urls import path, include
from website.views import *

app_name = 'website'

urlpatterns = [
    path('',home_page,name='index'),
    path('contact',contact_page,name='contact'),
    path('about',about_page,name='about'),
    path('newsletter',newsletter_page,name='newsletter')
]
