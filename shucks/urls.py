from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search-results'),
    path('categories/', views.categories, name='categories'),
    path('brands/', views.brands, name='brands'),
    path('products/', views.products, name='products'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('category-products/<int:category_id>/', views.category_products, name='category-products'),
    path('brand-products/<int:brand_id>/', views.brand_products, name='brand-products'),
    path('product/<str:slug>/<int:id>/', views.product_details, name='product-details'),
    # path('filter-data',views.filter_data,name='filter_data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)