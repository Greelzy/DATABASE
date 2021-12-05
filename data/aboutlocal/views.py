from django.shortcuts import render
from party.models import *


# Create your views here.
def about(request):
    context = {}
    local = LocalsParty.objects.all()
    context['local'] = local
    return render(request, 'local/localAll.html', context=context)


def localID(request, id_local):
    context = {}
    local = LocalsParty.objects.get(id=id_local)
    context['local'] = local
    return render(request, 'local/localAbout.html', context=context)
