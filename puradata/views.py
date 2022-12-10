from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory

from .models import Order, Orderline, Category, Professional, Customer, Debt, ProfessionalPayment
from .forms import CustomerForm, ProfessionalPaymentForm, CategoryForm, ProfessionalForm, OrderlineForm, ProductForm
# Create your views here.


def home(request):
    return render(request, 'puradata/index.html')

# region data_visualization


def view_customers(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'puradata/view_customers.html', context)


def view_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {
        'customer': customer,
    }
    return render(request, 'puradata/view_customer.html', context)


def view_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'puradata/view_categories.html', context)


def view_debts(request):
    debts = Debt.objects.all()
    context = {
        'debts': debts,
    }
    return render(request, 'puradata/view_debts.html', context)


def view_professionals(request):
    professionals = Professional.objects.all()
    context = {
        'professionals': professionals,
    }
    return render(request, 'puradata/view_professionals.html', context)


def view_professional_payments(request):
    professional_payments = ProfessionalPayment.objects.all()
    context = {
        'professional_payments': professional_payments,
    }
    return render(request, 'puradata/view_professional_payments.html', context)

# endregion data_visualization

# region data_creation


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
    context = {
        'form': form,
        'page_title': 'Cliente'
    }
    return render(request, 'puradata/add_data.html', context)


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
    context = {
        'form': form,
        'page_title': 'Profesional'
    }
    return render(request, 'puradata/add_data.html', context)


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
    context = {
        'form': form,
        'page_title': 'Categoria'
    }
    return render(request, 'puradata/add_data.html', context)


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
    context = {
        'form': form,
        'page_title': 'Pago de Profesional'
    }
    return render(request, 'puradata/add_data.html', context)


def add_order(request, pk):
    '''
    Add order to an specific customer
    This whole implementation needs to be redone, because this code is awful
    '''
    # First we get the customer
    customer = get_object_or_404(Customer, id=pk)
    OrderlineFormSet = formset_factory(OrderlineForm, extra=3)
    formset = OrderlineFormSet()
    if request.method == 'POST':
        formset = OrderlineFormSet(request.POST)
        if formset.is_valid():
            # Create a new order, and assign the customer to it
            new_order = Order.objects.create(customer=customer)
            for form in formset:
                form = form.cleaned_data
                print(form)
                # When the user inputs nothing on one of the forms, it exits the loop
                if form == {}:
                    break
                # Create a new orderline for each form and assing it to the order
                new_orderline = Orderline.objects.create(
                    order=new_order,
                    product=form['product'],
                    professional=form['professional'],
                    cash_payment=form['cash_payment'],
                    mercado_pago_payment=form['mercado_pago_payment']
                )
        else:
            print("The formset was not valid displaying important info:")
            print(request.POST)
            print(f"Errors: {formset.errors}")
            print(f"Is it bound?: {formset.is_bound}")
    context = {'customer': customer, 'formset': formset}
    return render(request, 'puradata/add_order.html', context)


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
    context = {
        'form': form,
        'page_title': 'Producto'
    }
    return render(request, 'puradata/add_data.html', context)

# endregion data_creation
