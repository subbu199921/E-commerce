from django.shortcuts import render
from .models import Product, Customer, Cart, Order
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


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

def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the product is in stock
    if product.stock > 0:
        product.stock -= 1  # Reduce stock by 1
        product.save()      # Save the updated product
        messages.success(request, f"Your order for '{product.name}' was placed successfully! 🎉")
    else:
        messages.error(request, f"Sorry, '{product.name}' is out of stock.")

    # Redirect back to the products page
    return redirect('products')


def orders_page(request):
    orders = Order.objects.all().order_by('-ordered_at')
    return render(request, 'orders.html', {'orders': orders})