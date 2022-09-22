from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import CreateUserForm
from .models import User

def index(request):

	if request.method == 'POST':
		userForm = CreateUserForm(request.POST)
		if userForm.is_valid():
			user = User(name=request.POST['name'], surname=request.POST['surname'])
			user.save()

	users = User.objects.all()

	userForm = CreateUserForm()

	template = loader.get_template('xss/index.html')
	context = {	'users': users,
				'form': userForm }

	return HttpResponse(template.render(context, request))

def reset(request):
	if request.method == 'POST':
		
		users = User.objects.all().delete()

		u1 = User(name="Nicola", surname="Iommazzo")
		u1.save()
		u2 = User(name="Nic", surname="Iom")
		u2.save()
		u3 = User(name="name", surname="surname")
		u3.save()

		return HttpResponseRedirect('/xss')
