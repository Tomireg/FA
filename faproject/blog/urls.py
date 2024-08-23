from django.urls import path
from .views import PostlistView #Changed here
from .import views

urlpatterns = [
    path('', PostlistView.as_view(), name='blog-home'), #Changed here
    path('about/',views.about, name='blog-about'),
]