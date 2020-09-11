from django.shortcuts import render, redirect
from .models import Voluntary
from .forms import VoluntaryForm


def create_voluntary(request):
    if request.method == 'POST':
        form = VoluntaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
            form = VoluntaryForm()
    return render(request, 'core/create_voluntary.html', {'form':form})


def list_voluntary(request):
    lista = Voluntary.objects.all()
    return render(request, 'core/list_voluntary.html', {'lista':lista})