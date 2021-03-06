from django.shortcuts import render
from api.stats import get_points, get_name, get_events
from api.config import config

def home(request):
	return render(request, 'home.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')

def account(request):
	return render(request, 'account.html', {'points': get_points(request), 'name': get_name(request), 'events': get_events(request)})

def submit(request):
	return render(request, 'submit.html')

def handler500(request):
	return render(request, '500.html')

def handler404(request):
	return render(request, '404.html')

def handler403(request):
	return render(request, '403.html')

def handler400(request):
	return render(request, '400.html')

class admin:
	def home(request):
		if 'admin' in request.session:
			return render(request, 'admin.html')
		else:
			return render(request, 'auth.html')
	def raffle(request):
		if 'admin' in request.session:
			return render(request, 'raffle.html')
		else:
			return render(request, 'auth.html')
	def event(request):
		if 'admin' in request.session:
			return render(request, 'add_event.html')
		else:
			return render(request, 'auth.html')
	def register(request):
		if config.ADMIN_CREATE or 'admin' in request.session:
			return render(request, 'create_admin.html')
		else:
			return render(request, 'auth.html')
