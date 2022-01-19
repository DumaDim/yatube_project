from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.group_posts),
    path('group/<int:pk>/',
        views.group_posts_1)
] 