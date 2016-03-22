from django.shortcuts import render


def cliente_list(request):
    return render(request, 'cliente/cliente_list.html', {})
# Create your views here.
