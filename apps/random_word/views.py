from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
	return render(request, 'random_word/index.html')


def random(request):
	if request.method == "POST":
		request.session['counter'] += 1
		request.session['random'] = get_random_string(length=14)
		print request.session['counter']
	return redirect("/random_word")

# Create your views here.
