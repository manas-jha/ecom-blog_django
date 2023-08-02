from django.contrib import admin
from django.urls import path
#by manas
from . import views

urlpatterns = [
    path('', views.index, name="blogHome"),
    path('blogpost/<int:id>', views.blogpost, name="blogPost"),
]