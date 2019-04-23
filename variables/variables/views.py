from .models import Variable
from django.shortcuts import render, redirect
from .forms import VariableForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def VariableList(request):
    queryset = Variable.objects.all()
    if request.META['HTTP_ACCEPT'] == 'application/json':
        context = list(queryset.values('id', 'name'))
        return JsonResponse(context, safe=False)
    else:
        context = {'variable_list': queryset}
        return render(request, 'Variable/variables.html', context)

def VariableCreate(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            measurement = form.save()
            measurement.save()
            messages.add_message(request, messages.SUCCESS, 'Variable create successful')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = VariableForm()

    context = {
        'form': form
    }

    return render(request, 'Variable/variableCreate.html', context)