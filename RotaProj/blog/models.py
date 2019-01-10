from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#call the blog app - noticeboard or board

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now) #maybe use auto_now_add=True in the future
  author = models.ForeignKey(User, on_delete= models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    # return reverse('post_detail', kwargs={'pk': self.pk})
    return reverse('blog-home')

class Todo(models.Model):  # create a new app just for todo lists named task list, model: Task
  # post = models.ForeignKey(Post, on_delete= models.CASCADE)
  text = models.CharField(max_length=40)
  done = models.BooleanField(default=False)
  created_at = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.text