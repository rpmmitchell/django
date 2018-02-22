from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'amadon/index.html')

def checkout(request):
	return render(request, 'amadon/checkout.html')

def buy(request):
	if request.method == "POST":
		request.session['product_id'] = request.POST['product_id'],
		request.session['quantity'] = request.POST['quantity'],
		if request.session['product_id'][0] == '1010':
			price = 19.99 * int(request.session['quantity'][0])
		if request.session['product_id'][0] == '1020':
			price = 29.99 * int(request.session['quantity'][0])
		if request.session['product_id'][0] == '1030':
			price = 4.99 * int(request.session['quantity'][0])
		if request.session['product_id'][0] == '1040':
			price = 49.99 * int(request.session['quantity'][0])
	request.session['price'] = price
	request.session['total'] += price

	print request.session['product_id'][0]
	print request.session['quantity'][0]
	print price
	return redirect('/checkout')
# Create your views here.
