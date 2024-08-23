from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView # UpdateView import added
)
from django.http import HttpResponse
from .models import Post

# Create your views here.x
def home(request):
    context = {
       'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] 

class PostDetailView(DetailView):
    model = Post  
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UpdateView): # New class created and UpdateView passed in.
    model = Post
    fields = ['title', 'content']
     
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
         

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})