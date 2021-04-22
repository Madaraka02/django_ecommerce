from django.shortcuts import render
# from django.http import JsonResponse,HttpResponse
# from django.template.loader import render_to_string
from .models import *

# Create your views here.
def home(request):
    ads = Advert.objects.all().order_by('-id')
    data = Product.objects.filter(is_featured=True).order_by('-id')
    return render(request, 'shucks/home.html', {'data':data, 'ads':ads})

def categories(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'shucks/categories.html', {'data':data})

def brands(request):
    data = Brand.objects.all().order_by('-id')
    return render(request, 'shucks/brands.html', {'data':data})    

def products(request):
    data = Product.objects.all().order_by('-id')

    return render(request, 'shucks/products.html', 
    {
        'data':data,

        
    })     
     

def brand_products(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    data = Product.objects.filter(brand=brand).order_by('-id')
    return render(request, 'shucks/brand-products.html', 
    {
        'data':data,
    })
def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    data = Product.objects.filter(category=category).order_by('-id')
    return render(request, 'shucks/category-products.html', 
    {
        'data':data,
    })       
    #product details page
def product_details(request, slug, id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request, 'shucks/product-details.html', {'data':product, 'related':related_products})     

# search 
def search(request):
    q = request.GET['q']
    data = Product.objects.filter(name__icontains=q).order_by('-id')
    return render(request, 'shucks/search.html', {'data':data})    

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items, 'order':order}        
    return render(request, 'shucks/cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items, 'order':order} 
    return render(request, 'shucks/checkout.html', context)    