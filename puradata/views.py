from django.shortcuts import render, redirect

from .models import Order, Orderline, Category, Professional, Customer, Debt, ProfessionalPayment
from .forms import CustomerForm, ProfessionalPaymentForm, CategoryForm, ProfessionalForm, OrderForm, ProductForm
# Create your views here.


def home(request):
    return render(request, 'puradata/index.html')


def add_customer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puradata:home')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()

    return render(request, 'puradata/add_data.html', {'form': form})


def add_professional(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puradata:home')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfessionalForm()

    return render(request, 'puradata/add_data.html', {'form': form})


def add_category(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puradata:home')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryForm()

    return render(request, 'puradata/add_data.html', {'form': form})


def add_professional_payment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfessionalPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puradata:home')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfessionalPaymentForm()

    return render(request, 'puradata/add_data.html', {'form': form})


def add_order(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puradata:home')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'puradata/add_data.html', {'form': form})


def add_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('puradata:home')
            # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductForm()

    return render(request, 'puradata/add_data.html', {'form': form})
