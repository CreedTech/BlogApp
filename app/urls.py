from django.urls import path
from app.views import *

urlpatterns = [
    path('',index,name='index'),
    path('blog/',blog,name='blog'),
]