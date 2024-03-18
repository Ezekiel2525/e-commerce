from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from  .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.db import IntegrityError


# Create your views here.
def index(request):
    products = Products.objects.order_by('-id')
    context = {'products' : products}
    return render (request, 'core/index.html', context)
 
 
def search(request):
    if request.method == "GET":
        searched = request.GET.get("query")
        if searched:
            items = Products.objects.filter(product_name__icontains=searched)
            items = Products.objects.filter(price = float(searched))
            return render(request, 'core/searchpanel.html', {'items' : items})   
        else:
            print("No Information to show")
            return render(request, 'core/searchpanel.html')


@login_required        
def sell(request):
    if request.method == 'POST':
        pro_from = ProductsForm(request.POST, request.FILES)
        if pro_from.is_valid():
            pro_from.save()
            messages.success(request, 'Product Uploaded successfully')
            return redirect('index')
        
    else:
        pro_from = ProductsForm()
    
    context = {'pro_form' : pro_from}
    
    return render(request, 'core/sell.html', context)


class ProductsDetailView(DetailView):
    model = Products
    template_name =   'core/product.html'
    context_object_name = 'product'

   
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_totals =[]
    total_price = 0
    for item in cart_items:
        item_total = item.product.discount * item.quantity
        item_totals.append(item_total)
        total_price += item_total
    item_with_total = zip(cart_items, item_totals)    
    return render(request, 'core/cart.html', {'total_price' : total_price, 'item_with_total' : item_with_total})   


def add_to_cart(request, pk):
    product = Products.objects.get(pk=pk)
    try:
        cart_item = CartItem.objects.get(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        try:
            cart_item = CartItem.objects.create(product=product, user=request.user, quantity=1)
        except IntegrityError as e:

            print(f"IntegrityError: {e}")

    return redirect('cart')


def subtract_from_cart(request, pk):
    product = get_object_or_404(Products, pk=pk)
    cart_item = get_object_or_404(CartItem, product=product, user=request.user)

    cart_item.quantity -= 1
    if cart_item.quantity <= 0:
     cart_item.delete()
    else:
        cart_item.save()

    return redirect('cart')

def increase_cart_quantity(request, pk):
    product = get_object_or_404(Products, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        cart_item.quantity +=1
        cart_item.save()

    else:
        pass

    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart')

  
def store(request):
    return render (request, 'core/store.html')
    
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_totals =[]
    total_price = 0
    for item in cart_items:
        item_total = item.product.discount * item.quantity
        item_totals.append(item_total)
        total_price += item_total
    item_with_total = zip(cart_items, item_totals) 
    if request.method == 'POST':
        bill_form = UserBillingForm(request.POST)
        if bill_form.is_valid():
            billing = bill_form.save(commit=False)
            billing.user = request.user
            billing.save()
            return redirect('index')    
    else:
        bill_form = UserBillingForm()

    context = {'bill_form' : bill_form, 'item_with_total' : item_with_total, 'total_price' : total_price}
    return render (request, 'core/checkout.html', context)



    

def product(request):
    return render (request, 'core/product.html')
    

def about(request):
    return render (request, 'core/about.html') 

def contact(request):
    return render (request, 'core/contact.html')
