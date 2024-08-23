from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView # Import here
)
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), #Url pattern here
    path('about/',views.about, name='blog-about'),
]