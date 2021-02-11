from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	following=models.ManyToManyField(User,related_name='following',blank=True)
	bio=models.TextField(default='Empty...')
	updated=models.DateTimeField(auto_now=True)
	create=models.DateTimeField(auto_now_add=True)

	def profile_posts(self):
		pass

	def __str__(self):
		return str(slef.user.username)
	class Meta:
		ordering=('-create',)