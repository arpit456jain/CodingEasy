from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() 
        context = super(PostListView, self).get_context_data( *args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content','image','category']
    success_message = "Your post was successfully created!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'content','image','category']
    success_message = "Your post was successfully updated!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_url = '/blog'
    success_message = "Your post has been successfully deleted!"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
class PostCategoryListView(ListView):
    model = Post
    template_name = 'blog/posts_by_category.html'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return Post.objects.filter(category=self.category).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super(PostCategoryListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class CategoryDetailView(DetailView):
    model = Category


# def CategoryView(request,pk):
#     category_posts = Post.objects.filter(category=pk)
#     category_name = Category.objects.get(id=pk)
#     return render(request, 'blog/categories.html',{'category_name':category_name,'category_posts':category_posts})


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ['name']
    success_message = "Your category was successfully created!"

    def form_valid(self, form):
        form.instance.catrgory_author = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['name']
    success_message = "Your category was successfully updated!"

    def form_valid(self, form):
        form.instance.catrgory_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.catrgory_author:
            return True
        return False


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Category
    success_url = '/blog'
    success_message = "Your category has been successfully deleted!"

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.catrgory_author:
            return True
        return False


def LastFivePosts(request):
    last_five_posts = Post.objects.all().order_by('-date_posted')[:5]
    return render (request,'blog/lastFivePosts.html',{'last_five_posts':last_five_posts})

def LatestJobs(request):
    category_num = Category.objects.filter(name="Jobs").first()
    latest_jobs = Post.objects.filter(category=category_num).order_by('-date_posted')[:5]
    return render (request,'blog/latestJobs.html',{'latest_jobs':latest_jobs})


def search(request):
    if request.method == 'POST':
        search_content = request.POST['search_content']
        lookup = (Q(title__icontains=search_content) or Q(content__icontains=search_content))
        posts = Post.objects.filter(lookup)
        return render(request, 'blog/post_search_result.html', {'search_content': search_content, 'posts': posts})
    else:
        return render (request,'blog/post_search_result.html',{})