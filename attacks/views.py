from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AttackForm

from django.forms.models import model_to_dict
from django.http import JsonResponse


from .models import Attack

import json

def index(request):
    context = {'attacks': Attack.objects.all()}
    return render(request, 'attacks/index.html',context)

def attack(request, attack_id):
    attack = Attack.objects.get(id=attack_id)
    return JsonResponse(model_to_dict(attack))

def attacks(request):
    attacks = Attack.objects.all()
    return JsonResponse([model_to_dict(attack) for attack in attacks], safe=False)

def new_attack(request):
    if request.method == 'POST':
        form = AttackForm(request.POST)
        if form:
            form = form.save()
            return HttpResponseRedirect('/')
    else:
        form = AttackForm()
    return render(request, 'attacks/new_attack.html', {'form': form})

def stop_attacks(request):
    attack_ids = json.loads(request.body)['attack_ids']
    print(attack_ids)
    for attack_id in attack_ids:
        attack = Attack.objects.get(id=attack_id)
        # TODO: add logic to stop attack
        attack.status = Attack.AttackStatus.STOPPED
        attack.save()
    return HttpResponseRedirect('/')