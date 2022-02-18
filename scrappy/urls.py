from django.urls import path, include
from . import views

urlpatterns = [
    path('search_id', views.search_id, name='search_id'),
    path('search_class', views.search_class, name='search_id'),
    path('search_el', views.search_el, name='search_id'),
    path('', views.index, name='index'),
]