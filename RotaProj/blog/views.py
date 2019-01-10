from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from .models import Post, Todo

from .forms import TodoPostForm

class PostListView(ListView):
  model = Post
  template_name = 'blog/blog_home.html'
  context_object_name = 'posts'
  extra_context = {'title':'Board',}
  ordering = ['-date_posted']
  paginate_by = 4


class PostDetailView(DetailView):
  model = Post
  # template_name = 'blog/blog_detail.html'
  # context_object_name = 'posts'
  extra_context = {'title':'Detail',}
  

class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']
  extra_context = {'title':'Create',}
  # success_url = 'home-blog'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']
  extra_context = {'title':'Create',}
  # success_url = 'home-blog'

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  extra_context = {'title':'Detail',}
  success_url = '/blog/'


  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False


def todo_list(request):
  todos = Todo.objects.all().order_by("-created_at")

  todo_form = TodoPostForm()

  context = {
    'todos':todos,
    'todo_form':todo_form
  }
  return render(request, "blog/todo.html", context)

@require_POST
def create_todo_list_post(request):
  todo_form = TodoPostForm()

  if request.method == 'POST':
    todo_form = TodoPostForm(request.POST)

    if todo_form.is_valid():
      todo_form.save()
  
  return redirect("todo_list")

def complete_todo(request, pk):
  todo = get_object_or_404(Todo, pk=pk)
  todo.done = True
  todo.save()
  return redirect("todo_list")


def remove_todo(request, pk):
  todo = get_object_or_404(Todo, pk=pk)
  todo.delete()
  return redirect("todo_list")


def remove_completed_todo(request):
  Todo.objects.filter(done__exact=True).delete()
  return redirect("todo_list")


def remove_all_todos(request):
  Todo.objects.all().delete()
  return redirect("todo_list")


