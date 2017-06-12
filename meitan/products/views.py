from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from models import Product, Category
from django.http import HttpResponse
from cart.forms import CartAddProductForm, CartAddProductFormDetail
from cart.cart import Cart
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from endless_pagination.decorators import page_template


class CategoryListView(TemplateView):

    template_name = "products/product_list.html"

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST' and self.request.is_ajax():
            project_id = self.request.POST.get('changePrice', '')
        else:
            project_id = 0



        active_category_id = self.request.GET.get('category_id')
        main_categories = Category.get_main_categories()
        print project_id
        cart_product_form = CartAddProductForm()
        add_product_id = self.request.GET.get('category_id')


        url = self.request.get_full_path()



        self.request.session['url'] = url

        print url


        if not active_category_id:
            products = Product.objects.all()
            active_category = None

            #print Cart.__len__()
            print products
        else:
           # active_category_id = int(active_category_id)
            products = Product.objects.filter(category_id = int(active_category_id))
            active_category = Category.objects.get(id=int(active_category_id))


        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)

        context = super(CategoryListView, self).get_context_data(**kwargs)

        # context['categories'] = ServiceCategory.objects.filter(parent_id = active_category_id)
        context['products'] = products
        context['series'] = Product.objects.all()
        context['active_category_id'] =  active_category_id
        context['active_category'] = active_category
        context['cart_product_form'] = cart_product_form
        return context

class ProductView(TemplateView):
   template_name = "products/product_detail.html"

   def get_context_data(self, **kwargs):

        product = get_object_or_404(Product, slug = self.kwargs.get('slug'))
        #product = Product.objects.get(slug = self.kwargs.get('slug'))

        active_category = Category.objects.get(products = product.id)
        related_products = Product.objects.filter(category_id = product.category_id, recommended=True)
        cart_product_form_detail = CartAddProductFormDetail()

        url = self.request.get_full_path()

        self.request.session['url'] = url

        print url

        context = super(ProductView, self).get_context_data(**kwargs)

        context['related_products'] = related_products
        context['cart_product_form_detail'] = cart_product_form_detail
        context['product'] = product
        #context['active_category_id'] =  active_category_id
        context['active_category'] = active_category
        context['active_category_id'] = int(active_category.id)
        #context['cart_product_form'] = cart_product_form
        return context



@require_POST
def CartAdd(request, product_id):
    cart = Cart(request)
    print cart
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        x = request.get_full_path()
        cd = form.cleaned_data
        cart.add(product=product, quantity=1,
                                 update_quantity=cd['update'])
    else:
        print 'lox'

    url = request.session['url']
    print x
    return redirect(url)

@require_POST
def CartAddDetail(request, product_id):
    cart = Cart(request)
    #print cart
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductFormDetail(request.POST)
    if form.is_valid():
        x = request.get_full_path()
        cd = form.cleaned_data
        quantity=cd['quantity']
        print quantity


        cart.add(product=product, quantity=cd['quantity'],
                                 update_quantity=cd['update'])
    else:
        print 'lox'

    url = request.session['url']
    print x
    return redirect(url)

def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    url = request.session['url']
    cart.remove(product)
    return redirect(url)

@require_POST
def offer(request):
    cart = Cart(request)
    #print cart
    form = SaleForm(request.POST)
    if self.request.method == "GET" and 'offer' in self.request.GET:
        form = SaleForm(self.request.GET)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sale_price = teacher
            sale.created = timezone.now()
            sale.save()
            print form
    return redirect('/')

@csrf_exempt
def filter_product(request):

    active_category_id = request.GET.get('category_id')
    main_categories = Category.get_main_categories()
    cart_product_form = CartAddProductForm()
    add_product_id = request.GET.get('category_id')
    url = request.get_full_path()
    request.session['url'] = url
    value_products = Product.objects.filter(category_id = int(active_category_id))

    if active_category_id:
        if request.method == 'POST' and request.is_ajax():
            price_value = request.POST.get('changePrice', '')
            param = request.POST.get('changeParams', '')
            series = request.POST.get('changeSeries', '')
            active_category = Category.objects.get(id=int(active_category_id))

            if param == 'forPrice':
                param = 'price'
            if param == 'forSeries':
                param = 'subtitle'
            if param == 'forNew':
                param = '-created'


            if price_value and param and series:
                products = Product.objects.filter(price__gte = price_value).filter(subtitle = str(series)).filter(category_id = int(active_category_id)).order_by(str(param)) 
                print products
            elif price_value:
                products = Product.objects.filter(price__gte = price_value).filter(category_id = int(active_category_id))
            elif price_value and param:
                products = Product.objects.filter(price__gte = price_value).filter(category_id = int(active_category_id)).order_by(str(param))
            elif price_value and series:
                products = Product.objects.filter(price__gte = price_value).filter(category_id = int(active_category_id)).order_by(str(param))
            elif param and series:
                products = Product.objects.filter(category_id = int(active_category_id)).filter(subtitle = str(series)).order_by(str(param))
            elif series:
                products = Product.objects.filter(subtitle = str(series)).filter(category_id = int(active_category_id))
            elif param:
                products = Product.objects.order_by(str(param))


            print price_value
            print param
            print series
            url = request.session['url']
            return render_to_response('products/product_list.html',{'products': products, 'active_category': active_category,  'value_products': value_products})
            #return render(request, 'products/product_list.html', {'products': products, 'value_products': value_products})
        else:
            price_value = request.POST.get('changePrice', '')
            param = request.POST.get('changeParams', '')
            series = request.POST.get('changeSeries', '')
            if price_value and param and series:
                products = Product.objects.filter(price__gte = price_value).filter(subtitle = series).filter(category_id = int(active_category_id)).order_by(param) 
            else:
                products = None
                active_category = Category.objects.get(id=int(active_category_id))
            return render_to_response('products/product_list.html', {'products': products, 'active_category': active_category,  'value_products': value_products})
    else:
        if request.method == 'POST' and request.is_ajax():
            price = request.POST.get('changePrice', '')
            param = request.POST.get('changeParams', '')
            series = request.POST.get('changeSeries', '')
            print price
            print param
            print series
            url = request.session['url']
            products = Product.objects.all()
            return render(request, 'product_list.html', {'products': products})
        else:
            products = Product.objects.all()
            active_category = None
            return render(request, 'products/product_list.html', {'products': products, 'active_category': active_category})


