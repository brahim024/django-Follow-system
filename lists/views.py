from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
def home_page(reuest):
	return HttpResponse('homa page')