from django.urls import path
from . import views
from .views import ContactView

urlpatterns = [
    path('', views.home, name='home-index'),
    path('courses/', views.courses, name='home-courses'),
    path('about/', views.about, name='home-about'),
    path('contact/', ContactView.as_view(), name='home-contact'),
]

    
