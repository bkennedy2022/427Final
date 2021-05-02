from django.shortcuts import render
from django.http import HttpResponse

import boto3
import pandas as pd

# Create your views here.


def home(request):
    return render(request,'caseMaps/home.html')

def chloropleth(request):
    return render(request,'caseMaps/chloropleth.html')

def histograms(request):
    return render(request,'caseMaps/histograms.html')

def regression(request):
    return render(request,'caseMaps/regression.html')