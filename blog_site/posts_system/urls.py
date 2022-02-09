from django.urls import path

from posts_system.views import post_creation_view, post_detail_view, post_list_view

app_name = 'blog_post'
urlpatterns = [
    #Posts System URLS
    path('feed/', post_list_view, name='blog_home'),
    path('<int:post_id>/', post_detail_view, name='blog_detail'),
    path('create_post/', post_creation_view, name='blog_create'),
]