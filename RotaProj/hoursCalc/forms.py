from django import forms
from .models import Shift

class ClockInOutForm(forms.ModelForm):
  clock_in = forms.TimeField(label='Clock In ', 
                             widget=forms.TimeInput( 
                             attrs={"class":""})) 

  clock_out = forms.TimeField(label='Clock Out', 
                              widget=forms.TimeInput(
                              attrs={"class":""}))

  break_time = forms.DurationField(label='Break', 
                                   widget=forms.TimeInput(
                                   attrs={"class":""}))

  date = forms.DateField(widget=forms.SelectDateWidget(attrs={"class":""}))

  class Meta():
    model = Shift 
    fields = ['name']

    # widgets={
    #   'name':forms.TextInput(attrs={"class":"XXXXX"} )
    # }



class SelectDateForm(forms.Form):
  date_from = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "",}, ), label="From")
  date_to = forms.DateField(widget=forms.SelectDateWidget(attrs={"class": "",}), label="To")

    

