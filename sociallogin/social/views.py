from django.shortcuts import render
from .models import Social
# Create your views here.
def home(request):
    socials = Social.objects
    return render(request, 'home.html', {'socials': socials})