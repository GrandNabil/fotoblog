from django.shortcuts import render
from django.contrib.auth import authenticate, login # importation des fonctions qui vont permetrre l'authentification
from . import forms

def login_page(request):
    forms = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connectés.'
            else:
                message = 'Identifiants invalides'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})
            
            


