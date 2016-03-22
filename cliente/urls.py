from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.cliente_list),
]
