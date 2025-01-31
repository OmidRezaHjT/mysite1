from django.urls import path, include
from website.views import home_page


urlpatterns = [
    path('',home_page)
]
