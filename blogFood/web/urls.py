from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from django.urls import path 
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.home , name = 'home'),
    path('upload/', views.upload, name = 'upload'),
    path('create', views.create , name = 'create'),
    path('author', views.author , name = 'author')
]
