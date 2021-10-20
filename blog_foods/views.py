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
    
def author(request):
    author = request.user
    posts = Post.objects.filter(posted_by_id=author.id)
    return render(request, 'author.html', {'author': author, 'posts': posts})
