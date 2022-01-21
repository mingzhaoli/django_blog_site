from django.shortcuts import render, get_object_or_404

from .models import Post
    
# Create your views here.

def post_list_view(request):
    post_list = Post.objects.order_by('-pub_date')[:10]
    context = {
        'post_list': post_list
    }
    return render(request, 'posts_system/post_list.html', context)

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts_system/post_detail.html', {'post': post})