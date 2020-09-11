from django.shortcuts import render, redirect
from .models import Actions
from .forms import ActionsForm


def create_actions(request):
    if request.method == 'POST':
        form = ActionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ActionsForm()
    return render(request, 'core/create_actions.html', {'form':form})


def list_actions(request):
    lista = Actions.objects.all()
    return render(request, 'core/list_actions.html', {'lista':lista})