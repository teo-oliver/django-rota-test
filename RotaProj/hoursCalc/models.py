from django.db import models
import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User # PermissionsMixin

#Todo: Start working on Forms (rewatch the udemy tutorials)

# Name Ideia: WorkIntheDjango

# Todo: change FloatField to DecimalField (duration-> set precision to 2 or rounding=ROUND_DOWN)
# https://docs.python.org/3/library/decimal.html#module-decimal

# Todo: SuperUser to the Manager (so only him/her can edit the spreadsheet)

# Todo: Total Week hour, Total Month Hours(view: from cut-off date to date) 

# Make a static folder for CSS and js scripts

# Make a html file, that loops dateTime objects, to create a calendar, that, check if theres a match between the name row and date column display on the "calendar field"
# https://www.w3schools.com/howto/howto_css_calendar.asp


# related_name on ForeignKey to use the _set, if not it will be the class name _set, for ex for Hours Day would be hoursday_set, from there you can use hoursday_set.all

# class User(User, PermissionsMixin)

#     def __str__(self):
#         return self.username


class Shift(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    clock_in = models.DateTimeField(blank=True, null=True)
    clock_out = models.DateTimeField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    duration  = models.FloatField(default=0)
    break_time = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ['date']

    def time_diff(self):
        if self.clock_out and self.clock_in:
            self.duration = (self.clock_out - self.clock_in).seconds/60/60
            if self.break_time:
                self.duration = self.duration - self.break_time.seconds/60/60
                self.duration = round(self.duration, 1)
            self.save()      
        else:
            return

    def __str__(self):
        return str(self.name)


class Week(models.Model):
    week = models.CharField(max_length=150, blank=True, null=True)
    month = models.ForeignKey('Month',on_delete=models.CASCADE)
    week_hours = models.FloatField(default=0)

    def __str__(self):
        return str(self.week)
    

class Month(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    month_name = models.CharField(max_length=150, blank=True, null=True)
    month_hours = models.FloatField(default=0)

    def __str__(self):
        return str(self.month_name)

    def total_month_hours(self):
        pass


     