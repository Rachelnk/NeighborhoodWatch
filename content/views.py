from django.shortcuts import render
from .models import Profile, Post, Neighborhood, Business
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
