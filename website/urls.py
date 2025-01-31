from django.urls import path, include
from website.views import *


urlpatterns = [
    path('',home_page),
    path('contact',contact_page),
    path('about',about_page)
]
