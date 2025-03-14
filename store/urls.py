from django.urls import path
from . import views
from .views import buy_product
from .views import orders_page

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('cart/', views.cart, name='cart'),
    path('orders/', views.orders, name='orders'),
    path('buy_product/<int:product_id>/', views.buy_product, name='buy_product'),

]
