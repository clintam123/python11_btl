from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    """Show all Post."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)

def upload(request):
    return render(request, 'upload.html')