from django.urls import path
from . import views

app_name = 'puradata'
urlpatterns = [
    path('', views.home, name="home"),
    path('add_customer', views.add_customer, name='add_customer'),
    path('add_professional', views.add_professional, name='add_professional'),
    path('add_professional_payment', views.add_professional_payment,
         name='add_professional_payment'),
    path('add_category', views.add_category, name='add_category'),
    path('add_order', views.add_order, name='add_order'),
    path('add_product', views.add_product, name='add_product'),
]
