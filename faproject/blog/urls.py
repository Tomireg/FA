from django.urls import path
from .views import PostListView #Changed here
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #Changed here
    path('about/',views.about, name='blog-about'),
]