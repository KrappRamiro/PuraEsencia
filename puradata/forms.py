from django.forms import ModelForm
from .models import Customer, Professional, Category, ProfessionalPayment, Order, Product


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ProfessionalForm(ModelForm):
    class Meta:
        model = Professional
        fields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProfessionalPaymentForm(ModelForm):
    class Meta:
        model = ProfessionalPayment
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
