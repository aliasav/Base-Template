from django.contrib.auth.models import User

class UserProfile(models.Model):
	# add user attributes here
	user = models.OneToOneField(User)