from .models import *
def get_filters(request):
    cats = Product.objects.distinct().values('category__title', 'category__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    sizes = Product.objects.distinct().values('size__title', 'size__id')
    colors = Product.objects.distinct().values('color__title', 'color__id','color__color_code')
    data = {
        'cats':cats,
        'brands':brands,
        'colors':colors,
        'sizes':sizes,

    }    
    return data   
