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

	def get_object(self,**kwargs):
		pk=self.kwargs.get('pk')
		view_profile=Profile.objects.get(pk=pk)
		return view_profile

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		view_profile=self.get_object()
		my_profile=Profile.objects.get(user=self.request.user)
		if view_profile.user in my_profile.following.all():
			follow=True
		else:
			follow=False

		context['follow']=follow
		return context
