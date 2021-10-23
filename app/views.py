from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def profile(request): # view profile
    current_user = request.user
    return render(request, 'profile.html')