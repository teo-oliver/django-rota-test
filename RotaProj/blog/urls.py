from django.contrib import admin
from django.urls import path
from . import views as blog_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth import views as auth_views

# app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/new/', PostCreateView.as_view(), name="post_create"), 
    path('todo/', blog_views.todo_list, name="todo_list"),
    path('todo/<int:pk>/', blog_views.complete_todo, name="complete_todo"),
    path('todo/submit/', blog_views.create_todo_list_post, name="todo_submit"), #add_todo
    path('todo/deletecomplete/', blog_views.remove_completed_todo, name="delete_complete"),
    path('todo/deleteall/', blog_views.remove_all_todos, name="delete_all"),
]
