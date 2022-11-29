from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.models import User



from authy.models import Profile



from django.template import loader


# Create your views here.


def UserProfile(request, username):
	user = get_object_or_404(User, username=username)
	profile = Profile.objects.get(user=user)

	

	template = loader.get_template('profile.html')

	context = {
		'profile':profile,

	}

	return HttpResponse(template.render(context, request))
