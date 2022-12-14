from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.

# TODO: Implement a way of handling debts.
# The program needs to show how much money the client has to pay, and from where that debt comes from


class Customer(models.Model):
    name = models.CharField(max_length=200)
    dni = models.CharField(max_length=20, blank=True, null=True)
    cuit = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Professional(models.Model):
    name = models.CharField(max_length=200)
    dni = models.CharField(max_length=20, blank=True, null=True)
    cuit = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    datetime = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    facturado = models.BooleanField(default=False)  # Para la facturacion

    def __str__(self):
        return f'{str(self.id)} - {self.created}'

    class Meta:
        ordering = ['-created']


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Orderline(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cash_payment = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    mercado_pago_payment = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"ID: {self.id}\tProduct: {self.product}"


class Debt(models.Model):
    # You should be able to delete Debts
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = MoneyField(
        max_digits=10, decimal_places=2, default_currency='ARS')

    def __str__(self):
        return f'{str(self.id)} - {self.customer}'


class ProfessionalPayment(models.Model):
    # Used to record payments to professionals
    professional = models.ForeignKey(Professional, on_delete=models.RESTRICT)
    amount = MoneyField(
        max_digits=10, decimal_places=2, default_currency='ARS')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.id)} - {self.created}'
