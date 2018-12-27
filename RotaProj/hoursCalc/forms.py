from django import forms
from .models import Shift
from django.contrib.auth.models import User


class ClockInOutForm(forms.ModelForm):
  clock_in = forms.TimeField(label='Clock In ', 
                             widget=forms.TimeInput( 
                             attrs={"class":"form-control", "placeholder":"hour:min:sec"})) 
  # clock_in = forms.TimeField(label='Clock In ', 
  #                            widget=forms.TimeInput( 
  #                            attrs={"class":"form-control"})) 

  clock_out = forms.TimeField(label='Clock Out', 
                              widget=forms.TimeInput(
                              attrs={"class":"form-control", "placeholder":"hour:min:sec"}))

  break_time = forms.DurationField(label='Break', 
                                   widget=forms.TimeInput(
                                   attrs={"class":"form-control", "placeholder":"hour:min:sec"}))

  date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class":""}))

  class Meta():
    model = Shift 
    fields = ['name']


class SelectDateForm(forms.Form):
  date_from = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "",}, ), label="From")
  date_to = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "",}), label="To")

    
class UserForm(forms.ModelForm):
  class Meta():
    model = User
    fields = ['username', 'email', 'password']
