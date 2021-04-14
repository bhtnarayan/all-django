"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from django.views.generic.base import TemplateView 
from accounts.views import Home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment_blog/', include('comment_blog.urls')),
    path('articles/', include('articles.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include('polls.urls')),
    path('sendemail/', include('sendemail.urls')), 
    path('apis/v1/', include('apis.urls')),
    path('cities/', include('cities.urls')),
    path('', Home.as_view(), name = 'home'), #new

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

