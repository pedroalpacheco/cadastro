from django.shortcuts import render
from django.utils import timezone
from .models import Post


def cliente_list(request):
    posts = Post.objects.filter()
    return render(request, 'cliente/cliente_list.html', {'posts': posts})
