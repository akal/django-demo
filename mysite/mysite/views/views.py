from django.shortcuts import render
from mysite.models import models


def home(request):
    return render(request, 'template.html', {'key': 'value'})

