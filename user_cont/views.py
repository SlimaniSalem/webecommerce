from django.http import HttpResponse
from django.shortcuts import render


def user_log(request):
    return render(request,'inscription.html')

