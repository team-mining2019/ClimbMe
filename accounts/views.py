from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import Http404

import logging

from .models import Profile



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            nickname = request.POST['nickname']
            profile = Profile(user=user, nickname=nickname)
            profile.save()
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request): #이건 if request.method == 'POST': 이거 필요 없다!!!
    auth.logout(request)
    return redirect('home')



@login_required()
def update(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'update.html', {'user': user})

def changed(request, user_id):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        choice = request.POST.get('my_choice_field', None)
        if choice in ["Freshman", "Sophomore", "Junior", "Senior"]:
            if choice is 'Freshman':
                choice = "FR"
            elif choice is "Sophomore":
                choice = "SO"
            elif choice is "Junior":
                choice = "JR"
            else:
                choice = "SR"
        
        user = get_object_or_404(User, pk=user_id) 
        user.profile.nickname = nickname
        user.profile.year_in_school = choice
        user.profile.save()

        #prof = Profile.objects.filter(user=user.username)
        #prof.nickname = nickname
        #prof.user = user
        #for obj in prof:
        #    print(obj)
        #    obj.save()
        return redirect('home')
    return render(request, 'update.html', {'user': user})

