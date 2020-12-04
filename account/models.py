from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Contact(models.Model):
	user_from=models.ForeignKey(User,related_name='rel_from_set',on_delete=models.CASCADE)
	user_to=models.ForeignKey(User,related_name='rel_to_set',on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now=True,db_index=True)
	class Meta:
		ordering=('-created',)
	def __str__(self):
		return f'{self.user_from} follows {self.user_to}'
user_model=User
user_model.add_to_class('following',
						models.ManyToManyField('self',
							through=Contact,
							related_name='followers',
							symmetrical=False))