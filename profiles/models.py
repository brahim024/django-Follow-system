from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
		return str(self.user.username)
	class Meta:
		ordering=('-create',)

@receiver(post_save,sender=User)

def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
		print('created',instance)
