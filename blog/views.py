from django.shortcuts import render
from django.contrib.auth.decorators import login_required #  restreindre l’accès à des pages pour que seuls les utilisateurs connectés puissent y accéder

@login_required
def home(request):
    return render(request, 'blog/home.html')

