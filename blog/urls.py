from django.urls import re_path
from . import views
from prueba2.views import post_pruebas

urlpatterns = [
    re_path(r'^$', views.home, name='base'),
    re_path(r'^list/', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^prueba/', post_pruebas, name='show_pruebas'),
]