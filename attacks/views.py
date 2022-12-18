from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AttackForm

from .models import Attack, Client

def index(request):
    context = {'attacks': Attack.objects.all()}
    return render(request, 'attacks/index.html',context)

def new_attack(request):
    if request.method == 'POST':
        form = AttackForm(request.POST)
        if form:
            form = form.save()
            return HttpResponseRedirect('/attacks/')
    else:
        form = AttackForm()
    return render(request, 'attacks/new_attack.html', {'form': form})
