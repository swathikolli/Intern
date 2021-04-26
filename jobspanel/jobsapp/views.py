from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
import json

from datetime import date


def index(request):
    data=open('jobsapp/data.json').read()
    j_data=json.loads(data);
    return render(request, "jobsapp/index.html",{
        "list":j_data
        })
      