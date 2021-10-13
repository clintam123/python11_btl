from django.urls import path
from . import views

app_name = 'blog_foods'

urlpatterns = [
    path('', views.index, name='index'),
]