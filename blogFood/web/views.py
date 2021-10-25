from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from web import forms
from .models import Post 


# Create your views here.

def home(request):
    posts = Post.objects.all() 
    context = {'posts': posts}
    tmp = Post.objects.last()
    return render(request, 'web/index.html',context)


def create(request):
    return render(request, 'web/create.html'); 

def upload(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        description = request.POST.get("description")
        caption = request.POST.get('caption')
        scores = request.POST.get('scores')
        price = request.POST.get('price')
        new_post = Post.objects.create(price = price, img = img, caption = caption , description = description, rate = scores, user = 'test')
        new_post.save()
    
    return redirect('/')

   

        

