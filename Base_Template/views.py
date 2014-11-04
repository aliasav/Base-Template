from Base_Template.forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response, RequestContext
from django.template import Context

def home(request):
	return render_to_response('index.html')

def register(request):
	print 'Register called'
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'user_img' in request.FILES:
				profile.user_img = request.FILES['user_img']
			#profile.save()

			print 'User registered'
			registered = True

		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response('registration/register.html' , {'user_form': user_form, 'profile_form':profile_form,'registered':registered} , context)