from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    # Pages
    path('', views.index, name='home-index'),
    path('feature/', views.feature, name='home-feature'),
    path('pricing/', views.pricing, name='home-pricing'),
    path('contact/', views.contact, name='home-contact'),
    path('login/', views.login, name='home-login'),
    # Courses
    path('html/', views.html, name='html'),
    path('html1/', views.html1, name='html1'),
    path('css/', views.css, name='css'),
    path('css1/', views.css1, name='css1'),
    path('js/', views.js, name='js'),
    path('js1/', views.js1, name='js1'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('bootstrap1/', views.bootstrap1, name='bootstrap1'),
    path('py/', views.py, name='py'),
    path('py1/', views.py1, name='py1'),
    path('cpp/', views.cpp, name='cpp'),
    path('cpp1/', views.cpp1, name='cpp1'),
    path('ml/', views.ml, name='ml'),
    path('ml1/', views.ml1, name='ml1'),
    path('course_video/', views.course_video, name='course_video')
]
