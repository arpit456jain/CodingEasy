from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('category/posts/<int:pk>',PostCategoryListView.as_view(), name='posts_by_category'),
    # path('category/detail/<int:pk>/', CategoryView, name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/update', CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'),
    path('lastFivePosts/', views.LastFivePosts, name='last_five_posts'),
    path('LatestJobs/', views.LatestJobs, name='latest_jobs'),
    path('search', views.search, name='search_post'),
]