from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import UUIDField

class UserProfile(models.Model):
	# add user attributes here
	user = models.OneToOneField(User)
	name = models.CharField(max_length=300, blank=True)
	guid = UUIDField(db_index=True, blank=True)
	user_img = models.ImageField(upload_to='user_images', blank=True)