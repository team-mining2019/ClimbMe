from django.shortcuts import render
from .models import Pofol
# Create your views here.

def pofol(request):
    pofols = Pofol.objects
    return render(request, 'pofol.html', {'pofols': pofols})