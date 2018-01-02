from django.shortcuts import render
from .models import student

# Create your views here.

def home(request):
	return render(request,'base.html')