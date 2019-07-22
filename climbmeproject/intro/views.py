from django.shortcuts import render
from .models import Info
# Create your views here.
def intro(request):
    infos = Info.objects
    return render(request, 'intro.html', {'infos' : infos})