from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView


# Create your views here.x
def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView)
	model = Post