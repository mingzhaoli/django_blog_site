"""blog_site URL Configuration

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

from posts_system.views import post_list_view, post_detail_view, post_creation_view
from user_system.views import user_creation_view, user_login_view

urlpatterns = [
    #Posts System URLS
    path('', post_list_view,name='blog_list'),
    path('<int:post_id>/', post_detail_view, name='blog_detail'),
    path('create_post/', post_creation_view, name='blog_create'),
    
    #User System URLS
    path('signup/', user_creation_view, name='user_signup'),
    path('login/', user_login_view, name='user_login'),

    #Admin System URLS
    path('admin/', admin.site.urls),
]
