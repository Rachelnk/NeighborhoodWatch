from django.shortcuts import render, redirect
from .models import Profile, Post, Neighborhood, Business
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def loginUser(request):
  return render(request, 'login.html')

@login_required(login_url='login')
def index(request):
  hood = Neighborhood.get_hoods()
  return render (request, 'index.html')

def signup(request):
  return render(request,'signup.html')