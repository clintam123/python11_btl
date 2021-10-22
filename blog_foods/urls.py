from django.urls import path
from . import views

app_name = 'blog_foods'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),  # 'Upload'
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('author/<int:user_id>', views.author, name='author_detail'),
    path('post/<int:post_id>', views.post, name='post_detail'),
]
