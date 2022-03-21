from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    extra_context = {'title': 'Blog'}


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'posts'
    extra_context = {'title': 'Blog'}


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    extra_context = {'title': 'Blog'}
    success_message = "Your post was successfully created!"


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    extra_context = {'title': 'Blog'}
    success_message = "Your post was successfully updated!"


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog'
    success_message = "Your post has been successfully deleted!"
    extra_context = {'title': 'Blog'}
