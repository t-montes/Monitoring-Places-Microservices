from .models import Measurement
from django.shortcuts import render, redirect
from .forms import MeasurementForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def MeasurementList(request):
    queryset = Measurement.objects.all().order_by('-dateTime')[:10]
    context = {
        'measurement_list': queryset
    }
    return render(request, 'Measurement/measurements.html', context)

def MeasurementCreate(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save()
            measurement.save()
            messages.add_message(request, messages.SUCCESS, 'Measurement create successful')
            return HttpResponseRedirect(reverse('measurementCreate'))
        else:
            print(form.errors)
    else:
        form = MeasurementForm()

    context = {
        'form': form
    }

    return render(request, 'Measurement/measurementCreate.html', context)