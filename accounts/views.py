from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def HomePage(request):
    context = {}
    return render(request, 'index.html', context)

def TestPage(request):
    context = {}
    return render(request,'test.html', context)

def ThanksPage(request):
    context = {}
    return render(request, 'thanks.html', context)

def signUpPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for: ' + username)
			return redirect('login')

	context = {'form': form}
	return render(request, 'signup.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('test')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('thanks')
