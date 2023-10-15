from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout # importation des fonctions qui vont permetrre l'authentification
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.views.generic import View
from django.urls import path
from . import forms


    