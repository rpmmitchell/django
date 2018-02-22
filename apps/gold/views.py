from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime

def index(request):
	if 'msg_gold' not in request.session: 
		request.session['msg_gold'] = ''
	if 'split' not in request.session:
		request.session['split'] = ''
	if 'gold' not in request.session:
		request.session['gold'] = 0
	return render(request, 'gold/index.html')

def money(request):
	if request.method == "POST":
		if request.POST['action'] == 'farm':
			x = random.randrange(10,20)
			request.session['gold'] += x
			request.session['msg_gold'] += 'You won ' + str(x) + ' gold from the farm! ' + '(' + strftime('%Y-%m-%d %I:%M %p') + ')' + '/n'
			request.session['split'] = request.session['msg_gold'].split('/n')
		if request.POST['action'] == 'cave':
			x = random.randrange(5,10)
			request.session['gold'] += x
			request.session['msg_gold'] += 'You won ' + str(x) + ' gold from the cave! ' + '(' + strftime('%Y-%m-%d %I:%M %p') + ')' + '/n'
			request.session['split'] = request.session['msg_gold'].split('/n')
		if request.POST['action'] == 'house':
			x = random.randrange(2,5)
			request.session['gold'] += x
			request.session['msg_gold'] += 'You won ' + str(x) + ' gold from the house! ' + '(' + strftime('%Y-%m-%d %I:%M %p') + ')' + '/n'
			request.session['split'] = request.session['msg_gold'].split('/n')
		if request.POST['action'] == 'casino':
			x = random.randrange(-50,50)
			request.session['gold'] += x
			if x > 0:
				request.session['msg_gold'] += 'You won ' + str(x) + ' gold from the casion! ' + '(' + strftime('%Y-%m-%d %I:%M %p') + ')' + '/n'
				request.session['split'] = request.session['msg_gold'].split('/n')
			else:
				request.session['msg_gold'] += 'You lost ' + str(abs(x)) + ' gold from the casion! ' + '(' + strftime('%Y-%m-%d %I:%M %p') + ')' + '/n'
				request.session['split'] = request.session['msg_gold'].split('/n')
	return redirect('/gold')

def reset(request):
	if request.method == "POST":
		del request.session['gold']
		del request.session['msg_gold']
		del request.session['split']
	print 'gold popped'
	return redirect('/gold')
