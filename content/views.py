from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Profile, Post, Neighborhood, Business
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def loginUser(request):
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)

      if not User.objects.filter(username=username).exists():
          messages.error(request, 'Username Does Not Exist! Choose Another One.')
          return redirect('login')

      if user is None:
        messages.error(request, 'Username/Password Is Incorrect! Please Try Again')
        return redirect('login')

      if user is not None:
        login(request, user)
        return redirect(reverse('index'))
  return render(request, 'login.html')

@login_required(login_url='login')
def logoutUser(request):
  logout(request)
  messages.success(request, 'Succesfully Logged Out')
  return redirect('login')

@login_required(login_url='login')
def index(request):
  hood = Neighborhood.objects.all()
  return render (request, 'index.html', {'hood': hood})

def signup(request):
  if request.method == 'POST':
    context= {'has_error': False}
    username = request.POST['username']
    email = request.POST['email']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
      messages.error(request,'Passwords do not match! Try Again.')
      return redirect('signup')

    if User.objects.filter(username=username).exists():
      messages.error(request,'Username Is Taken. Try Again.')
      return redirect('signup')

    if User.objects.filter(email=email).exists():
      messages.error(request, 'Email Address already taken. Try Again')
      return redirect('signup')

    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
    user.set_password(password1)
    user.save()
  return render(request,'signup.html')