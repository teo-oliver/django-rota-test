from django.contrib import admin
from .models import Shift, Week, Month
# Register your models here.

admin.site.register(Shift)
admin.site.register(Week)
admin.site.register(Month)

