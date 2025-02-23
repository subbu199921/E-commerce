from django.shortcuts import render
from .models import Product, Customer, Cart, Order

# Home page view
def home(request):
    return render(request, 'store/home.html')

# Products page view
def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

# Customers page view
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'store/customers.html', {'customers': customers})

# Cart page view
def cart(request):
    carts = Cart.objects.all()
    return render(request, 'store/carts.html', {'carts': carts})

# Orders page view
def orders(request):
    orders = Order.objects.all()
    return render(request, 'store/orders.html', {'orders': orders})