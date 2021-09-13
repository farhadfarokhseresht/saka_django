from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.http import HttpResponse ,QueryDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from .serializers import *
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
from .extra_Functions import *


def log_out(request):
    logout(request)
    return redirect('saka:signin')


def index(request):
    logout(request)
    return render(request, 'saka/index.html')


def signin(request):
    logout(request)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # ...
            user = form.get_user()
            login(request, user)
            return redirect('saka:labpage')
    else:
        form = AuthenticationForm()
    return render(request, 'saka/signin.html', {'form': form})


@login_required(login_url="/signin")
def labpage(request):
    user_lab_informations = Laboratory_info(request)
    try:
        user_lab_name = user_lab_informations['laboratory_name']
    except:
        user_lab_name = 'not lab found!'
    return render(request, 'saka/labpage.html', context={'user_lab_name': user_lab_name})


def test(request):
    print(old_days_data(request))
    return render(request, 'saka/test.html')


def formB(request):
    if request.method == "POST":
        a = QueryDict.get(request.POST,'search')
        # if a :
        print(QueryDict.get(request.POST,'day'))
        return redirect('saka:formB')
    else:
        context = {'old_days_data': old_days_data(request),
                   'backdate': old_days_data(request)[3],
                   'locfilde': 1,
                   'Latnumbers_info': Latnumbers_info(),
                   'selected_lat': Latnumbers_info()[0],
                   'Analyte_info': Analyte_info(),
                   'formcache': formcash(),
                   'Device_info': Device_info(request),
                   'Tmethod_info': Tmethod_info(request),
                   'Devicecompany_info': Devicecompany_info(request),
                   }
    return render(request, 'saka/formB.html', context=context)


@login_required(login_url="/signin")
def report(request):
    return render(request, 'saka/Report.html')
