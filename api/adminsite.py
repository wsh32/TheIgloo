from api.models import admin
from django.http import HttpResponse
from django.contrib.auth.hashers import *
import json, re, time

class account:

	def create_account(request):
		if (request.method != 'POST') or not all(x in request.POST for x in ['username', 'password', 'confirm']):
			return HttpResponse()

		username = request.POST['username']
		password = request.POST['password']
		confirm = request.POST['confirm']

		try:
			repeat_user = True
			admin.objects.get(username=username)
		except:
			repeat_user = False

		if len(username) == 0 or len(password) == 0:
			response = {'success': False, 'message': 'All fields must be filled out.'}
		elif repeat_user:
			response = {'success': False, 'message': 'Someone beat you to that username.'}
		elif re.search('[ -~]{1,40}', username).group() != username:
			response = {'success': False, 'message': 'DONT ACT LIKE YOU DIDNT KNOW THAT YOU ENTERED IN INVALID CHARACTERS TO TRY TO BREAK THE SITE!!'}
		elif password != confirm:
			response = {'success': False, 'message': 'If you cannot repeat your password you should change it.'}
		else:
			try:
				account = admin(user=username, password=make_password(password))
				account.save()

				response = {'success': True, 'message': 'Registration successful!'}
			except:
				response = {'success': False, 'message': 'Error. Try again in a few seconds.'}

		return HttpResponse(json.dumps(response), content_type="application/json")

class auth:
	def login(request):
		if (request.method != 'POST') or not all(x in request.POST for x in ['username', 'password']):
			return HttpResponse()

		if 'admin' in request.session:
			response = {'success': False, 'message': 'You are already logged in.'}
			return HttpResponse(json.dumps(response), content_type="application/json")

		try:
			m = admin.objects.get(user=request.POST['username'])
		except:
			m = False

		if hasattr(m, 'password') and check_password(request.POST['password'], m.password):
			request.session['admin'] = m.id
			response = {'success': True, 'message': 'You have logged in.'}
		else:
			response = {'success': False, 'message': 'Log in failed.'}
			time.sleep(0.5) # Prevent brute-forcing.

		return HttpResponse(json.dumps(response), content_type="application/json")

	def logout(request):
		'''Handles logout requests. Accepts no post parameters'''

		if 'admin' not in request.session:
			response = {'success': False, 'message': 'You are not logged in.'}
		else:
			request.session.flush()
			response = {'success': True, 'message': 'You have been logged out.'}

		return HttpResponse(json.dumps(response), content_type="application/json")