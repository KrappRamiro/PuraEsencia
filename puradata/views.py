from django.shortcuts import render, redirect, get_object_or_404
from django.forms import formset_factory

from .models import Order, Orderline, Category, Professional, Customer, Debt, ProfessionalPayment
from .forms import CustomerForm, ProfessionalPaymentForm, CategoryForm, ProfessionalForm, OrderlineForm, ProductForm, OrderForm
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


def view_orders(request):
    orders = Order.objects.all().order_by('datetime')
    context = {'orders': orders}
    return render(request, 'puradata/view_orders.html', context)

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


def add_order(request):
    '''
    Add order to an specific customer
    This whole implementation needs to be redone, because this code is awful
    '''
    OrderlineFormSet = formset_factory(OrderlineForm, extra=10)
    orderline_formset = OrderlineFormSet()
    order_form = OrderForm()
    if request.method == 'POST':
        orderline_formset = OrderlineFormSet(request.POST)
        order_form = OrderForm(request.POST)
        if orderline_formset.is_valid() and order_form.is_valid():
            # Create a new order, and assign the customer to it
            order_form = order_form.cleaned_data
            print(order_form)
            new_order = Order.objects.create(
                customer=order_form['customer'],
                datetime=order_form['datetime'],
            )
            # Create the orderlines and assign it to the order
            for form in orderline_formset:
                form = form.cleaned_data
                print(form)
                # When the user inputs nothing on one of the forms, it skips
                if form == {}:
                    continue
                # Create a new orderline for each form and assing it to the order
                new_orderline = Orderline.objects.create(
                    order=new_order,
                    product=form['product'],
                    professional=form['professional'],
                    cash_payment=form['cash_payment'],
                    mercado_pago_payment=form['mercado_pago_payment']
                )
        else:
            print(
                "The orderline_formset or the order_form was not valid displaying important info:")
            print("orderline_formset info:")
            print(request.POST)
            print(f"Errors: {orderline_formset.errors}")
            print(f"Is it bound?: {orderline_formset.is_bound}")
            print("\norder_form info:")
        return redirect('puradata:home')
    context = {'orderline_formset': orderline_formset,
               'order_form': order_form}
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
