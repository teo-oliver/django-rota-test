from django import forms
from .models import Todo


class TodoPostForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ['text']
