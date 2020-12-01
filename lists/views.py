from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import LaunchEvent


    #Create your views here.
def space_page(request):
    launches = LaunchEvent()
    return render(request, 'space_page.html', {'launches': launches})