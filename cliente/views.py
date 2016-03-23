from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def cliente_list(request):
    posts = Post.objects.filter()
    return render(request, 'cliente/cliente_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'cliente/cliente_detail.html', {'post': post})
