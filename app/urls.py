from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('',index,name='index'),
    path('blog/',blog,name='blog'),
    path('post-details/<str:slug>/',PostDetail,name='details'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
