"""CodingEasy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.registerPage,name='registerPage'),
    path('feature',views.feature,name='feature'),
    path('pricing',views.pricing,name='pricing'),
    path('html',views.html,name='html'),
    path('html1',views.html1,name='html1'),
    path('css',views.css,name='css'),
    path('css1',views.css1,name='css1'),
    path('js',views.js,name='js'),
    path('js1',views.js1,name='js1'),
    path('bootstrap',views.bootstrap,name='bootstrap'),
    path('bootstrap1',views.bootstrap1,name='bootstrap1'),
    path('py',views.py,name='py'),
    path('py1',views.py1,name='py1'),
    path('cpp',views.cpp,name='cpp'),
    path('cpp1',views.cpp1,name='cpp1'),
    path('ml',views.ml,name='ml'),
]
