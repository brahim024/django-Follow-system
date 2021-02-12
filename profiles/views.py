from django.shortcuts import render
from django.views.generic.detail import ListView,DetailView
from .models import Profile
# Create your views here.
class ProfileListView(ListView):
	model=Profile
	templates_name='profile/main.html'
	context_objects_name='profile'

	def get_queryset(self):
		profile=Profile.objects.all()exclude(user=self.request.user)
		
