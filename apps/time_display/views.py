from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
	context = {
		"time": strftime("%B,%d %Y %r", gmtime())
	}
	return render(request, 'main/index.html', context)

# Create your views here.
