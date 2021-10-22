from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.

def index(request):
    """Show all Post."""
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)

def upload(request):
    return render(request, 'upload.html')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post.html'
    
def author(request, user_id):
    singleAuthor = User.objects.get(id=user_id)
    posts = Post.objects.filter(posted_by_id=user_id)
    return render(request, 'author.html', {'singleAuthor': singleAuthor, 'posts': posts})

def post(request, post_id):
    singlePost = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'singlePost': singlePost})
