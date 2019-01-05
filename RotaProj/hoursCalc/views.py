from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Shift

from django.db.models import Sum, Count


def initial_page(request):
    return render(request, 'hoursCalc/initial_page.html')


@login_required
def index(request):

    # Calculate Interval and Save (todo: make it automatic outside the view on the models.py file)
    objects_id = list(Shift.objects.all().values_list('id', flat=True))
    for id in objects_id:
        ShiftObject = get_object_or_404(Shift, id=id)
        ShiftObject.time_diff()
    #####################################################################

    users = User.objects.all()
    form = forms.ClockInOutForm()
    shift = Shift.objects.all()

    context = {
        'shift': shift,
        'users': users,
        'form':form,      
    }

    return render(request, 'hoursCalc/index.html', context)


@login_required
def submitForm(request): #change to create_shift
    
    if request.method == 'POST':
        form = forms.ClockInOutForm(request.POST)

        if form.is_valid():  

            new_clock_in = str(form.cleaned_data['date'])+ ' ' + str(form.cleaned_data['clock_in'])  
            new_clock_out = str(form.cleaned_data['date'])+ ' ' + str(form.cleaned_data['clock_out'])

            Shift.objects.create(name=form.cleaned_data['name'], 
                                    clock_in=new_clock_in, 
                                    clock_out=new_clock_out,
                                    break_time = form.cleaned_data['break_time'],
                                    date=form.cleaned_data['date'],
                                    description=form.cleaned_data['description'] )
            
    return redirect(index)


@login_required       
def remove(request, pk): # change this to remove_shift
    post = get_object_or_404(Shift, pk=pk)
    post.delete()
    messages.success(request, f'Your shift has been removed')
    return redirect(index)


@login_required
def selectDate(request, dt="2000-01-01", df="2000-01-01" ): # juntar selectDate com select_periods

    users = User.objects.all()
    select_date_form = forms.SelectDateForm()
    shifts = Shift.objects.select_related('name').order_by('name')

    if request.method == 'POST':
        select_date_form = forms.SelectDateForm(request.POST)

        if select_date_form.is_valid():

            print("VALIDATION SUCCESS!")
            print("date_from: ", select_date_form.cleaned_data['date_from'])
            print("date_to: ", select_date_form.cleaned_data['date_to'])

            df = select_date_form.cleaned_data['date_from']
            dt = select_date_form.cleaned_data['date_to']
            
            shifts = Shift.objects.select_related('name').filter(date__gte=df, date__lte=dt).order_by('name')


    context = {
        'select_date_form': select_date_form,
        'users': users,
        'shifts':shifts,
        'title': 'Select Dates'
    }

    return render(request, 'hoursCalc/select.html', context)

    
@login_required
def select_periods(request, date_from, date_to): #do it so this function is not needed, change to filter

    users = User.objects.all()
    objects = Shift.objects.filter(date__gte=date_from).filter(date__lte=date_to)

    context = {
        'users': users,
        'objects':objects,
        
    }
    
    return render(request, 'hoursCalc/select.html', context)


@login_required
def update_shift(request, pk): #needs more work on this one
    
    shift_to_update = get_object_or_404(Shift, pk=pk)
   
    if request.method == 'POST':
        shift_form = forms.ShiftUpdateForm(request.POST)

        if shift_form.is_valid():  

            new_clock_in = str(shift_form.cleaned_data['date'])+ ' ' + str(shift_form.cleaned_data['clock_in'])  
            new_clock_out = str(shift_form.cleaned_data['date'])+ ' ' + str(shift_form.cleaned_data['clock_out'])

            shift_to_update.clock_in=new_clock_in    
            shift_to_update.clock_out=new_clock_out
            shift_to_update.break_time = shift_form.cleaned_data['break_time']
            shift_to_update.date=shift_form.cleaned_data['date']
                                             
            shift_to_update.save()
                                    
            messages.success(request, f'Your shift has been updated!')
            
            return redirect(index)    

    else:
        shift_form = forms.ShiftUpdateForm(initial={'clock_in':shift_to_update.clock_in,
                                                    'clock_out':shift_to_update.clock_out,
                                                   'date':shift_to_update.date,
                                                    'duration':shift_to_update.duration,
                                                    'break_time':shift_to_update.break_time,
                                                    'description':shift_to_update.description,                                                
        })


    context = {
        'shift_form':shift_form,
        # 'messages':messages
    }

    return render(request, 'hoursCalc/update_shift.html', context)



def shift_detail(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    return render(request, 'hoursCalc/shift_detail.html', {'shift':shift})







 # if request.method == 'POST':
    #     shift_form = forms.ClockInOutForm(request.POST, instance=request.shift)
                          
    #     if shift_form.is_valid():
    #         shift_form.save()
    #         messages.success(request, f'Your shift has been updated!')
    #         return redirect('index')

    # else:
    #     shift_form = forms.ClockInOutForm(instance=request.shift)