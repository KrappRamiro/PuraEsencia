from django.forms import ModelForm
from .models import Customer, Professional, Category, ProfessionalPayment, Orderline, Product


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


class OrderlineForm(ModelForm):
    class Meta:
        model = Orderline
        exclude = ['order']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
