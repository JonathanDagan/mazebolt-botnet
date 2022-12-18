from django.shortcuts import render
from django.http import HttpResponse
from .forms import AttackForm

from .models import Attack, Client

def index(request):
    context = {'attacks': Attack.objects.all()}
    return render(request, 'attacks/index.html',context)

def new_attack(request):
    form = AttackForm(request.POST)
    context = {'form': form}
    return render(request, 'attacks/new_attack.html', context)