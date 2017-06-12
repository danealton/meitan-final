from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm
#from cupons.forms import CuponApllyForm


#@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.GET)
    if form.is_valid():
        print form
        print cart
        cd = form.cleaned_data
        cart.add(product=product,quantity=1,
                                  update_quantity=cd['update'])
        show_success = True
    return redirect('/')


def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('/')

def CartDetail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })
    cupon_apply_form = CuponApllyForm()
    return render(request, 'cart/detail.html',
                 {'cart': cart})
