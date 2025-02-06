from django.urls import path, include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_page,name='index'),
    path('single',single_page,name='single'),
 
]
