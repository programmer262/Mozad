
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
@login_required
def cour(request):
    cours = Cour.objects.all()
    context = {'cours':cours}
    return render(request, 'docfiles.html', context)
@login_required
def exercice(request):
    exercices = Exercice.objects.all()
    context = {'exercices':exercices}
    return render(request, 'exercices.html', context)
@login_required
def correction(request):
    corrigés = Corrigé.objects.all()
    context = {'corrigés':corrigés}
    return render(request, 'correction.html', context)
  


def loginPage(request):
	if request.user.is_authenticated:
	     return redirect('cour')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('cour')
			else:
	 			messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required
def classe(request):
    classes = Classe.objects.all()
    context = {'classes':classes}
    return render(request, 'Live.html', context)
@login_required
def live(request):
    lives = Live_ended.objects.all()
    context = {'lives':lives}
    return render(request, 'endlives.html', context)
@login_required
def error(request):
    cours = Cour.objects.all()
    context = {'cours':cours}
    return render(request, 'courview.html', context)
