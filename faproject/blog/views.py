from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #Updated here. Now the default name is set equal to 'posts'
     
# Create your views here.x
def home(request):
    context = {
       'posts': Post.objects.all() #The view is looping over 'posts'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
