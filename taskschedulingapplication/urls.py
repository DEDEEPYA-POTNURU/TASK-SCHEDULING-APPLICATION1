"""taskschedulingapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from .views import index
from .views import trello
from .views import asana
from .views import podoist
from .views import notion
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name= 'index'),
    path('trello/',trello,name='trello'),
    path('asana/',asana,name='asana'),
    path('podoist/',podoist,name='podoist'),
    path('notion/',notion,name='notion'),
    path('accounts/', include('accounts.urls')), 
    path('forms/', views.forms, name='forms'),
    path('trello/', include('trello.urls')),
]
