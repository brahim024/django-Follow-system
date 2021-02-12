from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Profile
# Create your views here.
class ProfileListView(ListView):
	model=Profile
	templates_name='profiles/profile_list.html'
	context_object_name='profiles'

	def get_queryset(self):
		profile=Profile.objects.all().exclude(user=self.request.user)
		return profile

class ProfileDetail(DetailView):
	model=Profile
	templates_name='profiles/profile_detail'
