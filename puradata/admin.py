from django.contrib import admin

from .models import Professional, Category, Customer, Debt, Order, Orderline, ProfessionalPayment
# Register your models here.
admin.site.register([
    Professional,
    Category,
    Customer,
    Debt,
    Order,
    Orderline,
    ProfessionalPayment
])
