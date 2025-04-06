from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from products.models import Product
from order.models import Order
from django.core.paginator import Paginator
from .models import CustomUserModel



@login_required
def order_home(request):
    products = Product.objects.all()
    owner = request.user
    q = request.GET.get('q')
    if q and q!='None':
        products = Product.objects.filter(name__icontains = q)
    orders = Order.objects.filter(owner = owner)
    total = 0
    for i in orders:
        total = total + i.count
    orders = Order.objects.filter(owner = owner)
    return render(request, 'order/order_home.html', {'products': products,'q': q, 'total': total, 'orders': orders})



@login_required
def add_to_order(request, id):
    owner = request.user
    product = Product.objects.filter(id = id).first()
    if Order.objects.filter(product_id = product, owner = owner).exists():
        order = Order.objects.filter(product_id = product, owner = owner).first()
        order.count = order.count + 1
        order.save()
        return redirect('order:order_home')
    order = Order(product_id = product, count = 1, owner = owner)
    order.save()
    return redirect('order:order_home')

@login_required
def substract_to_order(request, id):
    owner = request.user
    product = Product.objects.filter(id = id).first()
    order = Order.objects.filter(product_id = product, owner = owner)
    if order.exists() and order.first().count != 1:
        order = Order.objects.filter(product_id = product, owner = owner).first()
        order.count = order.count - 1
        order.save()
        return redirect('order:order_home')
    elif order.first().count == 1:
        order.first().delete()
    return redirect('order:order_home')

@login_required
def view_order(request):
    owner = request.user
    orders = Order.objects.filter(owner = owner)
    products = []
    total = 0
    for i in orders:
        product = Product.objects.filter(id = i.product_id.id).first()
        products.append(product)
        total = total + i.count*product.price
    return render(request, 'order/view_order.html', context={'products': products, 'orders': orders, 'total': total})


@login_required
def addorder(request, id):
    owner = request.user
    product = Product.objects.filter(id = id).first()
    if Order.objects.filter(product_id = product, owner = owner).exists():
        order = Order.objects.filter(product_id = product, owner = owner).first()
        order.count = order.count + 1
        order.save()
        return redirect('order:view_order')
    order = Order(product_id = product, count = 1)
    order.save()
    return redirect('order:view_order')

@login_required
def substractorder(request, id):
    owner = request.user
    product = Product.objects.filter(id = id).first()
    order = Order.objects.filter(product_id = product, owner = owner)
    if order.exists() and order.first().count != 1:
        order = Order.objects.filter(product_id = product, owner = owner).first()
        order.count = order.count - 1
        order.save()
        return redirect('order:view_order')
    elif order.first().count == 1:
        order.first().delete()
    return redirect('order:view_order')