from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.core.paginator import Paginator
from .forms import CreateForm, EditForm
# Create your views here.

@login_required
def home(request):
    return render(request, 'products/home.html',)




@permission_required('products.add_product', raise_exception=True)
@login_required
def moderation(request):
    products = Product.objects.all()
    q = request.GET.get('q')
    if q and q!='None':
        products = Product.objects.filter(name__icontains = q)
    paginator = Paginator(products, 2)
    pnumber = request.GET.get('page')
    products = paginator.get_page(pnumber)
    return render(request, 'products/list.html', {'products': products,'q': q})


@permission_required('products.add_product', raise_exception=True)
@login_required
def create(request):
    if request.method == 'POST': 
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:moderation')
        return render(request, 'products/create.html', context={'form': form})
    form = CreateForm()
    return render(request, 'products/create.html', context={'form': form})



@permission_required('products.add_product', raise_exception=True)
@login_required
def delete(request, id):
    p = Product.objects.filter(id = id)
    p.delete()
    return redirect('products:moderation')


@permission_required('products.add_product', raise_exception=True)
@login_required
def view(request, id):
    p = Product.objects.filter(id = id).first()
    return render(request, 'products/view.html', context={'product': p})



@permission_required('products.add_product', raise_exception=True)
@login_required
def edit(request, id):
    if request.method == 'POST': 
        product = Product.objects.filter(id = id).first()
        form = EditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:moderation')
        return render(request, 'products/edit.html', context={'form': form})
    product = Product.objects.filter(id = id).first()
    form = EditForm(instance=product)
    return render(request, 'products/edit.html', context={'form': form, 'product': product})