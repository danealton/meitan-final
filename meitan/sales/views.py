from django.shortcuts import render, redirect
from cart.cart import Cart
from .forms import SaleForm
from products.models import Product
from django.utils import timezone
from django.core.mail import send_mail


def offer(request):
    cart = Cart(request)

    content = []

    for item in cart:
        title = item['product']
        quantity = item['quantity']
        price = item['total_price']

        content.append(str(title) + '__' + str(quantity) + '__' + str(price))
        #product=item.product
        #content.append(product.title)
    print content
    #print cart
    form = SaleForm(request.POST)
    if request.method == "GET" and 'offer' in request.GET:
        form = SaleForm(request.GET)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sale_price = cart.get_total_price()
            sale.content = content
            sale.created = timezone.now()
            sale.save()
            send_mail('test email', str(content),'alexrians@gmail.com', ['alexrians@gmail.com'])
            #print form
    return redirect('/')

# Create your views here.
