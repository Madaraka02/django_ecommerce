from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='1.Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='2. Brands'
    def __str__(self):
        return self.title  

class Size(models.Model):
    title = models.CharField(max_length=100)

    
    class Meta:
        verbose_name_plural='4. Sizes'
    def __str__(self):
        return self.title 


class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural='3. Colors'
    

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s;" ></div>' % (self.color_code))    
    def __str__(self):
        return self.title 

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)  
    is_featured = models.BooleanField(default=False)  
    
    class Meta:
        verbose_name_plural='5. Products'
    def __str__(self):
        return self.name  


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey( Color, on_delete=models.CASCADE)
    size = models.ForeignKey( Size, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_imgs/", null=True)

    class Meta:
        verbose_name_plural='6. ProductAttributes'

    def __str__(self):
        return self.product.name
        
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))    

class Advert(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ads_imgs/")

    def __str__(self):
        return self.title  

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, blank=True, null=True)
    transactio_id = models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property 
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property 
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total      

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property 
    def get_total(self):
        total = self.product.price * self.quantity
        return total



class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, null=True)
    phone_number = models.CharField(max_length=150, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location
