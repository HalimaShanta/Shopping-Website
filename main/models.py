from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.name
class Home(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=100, null=True)
    sub_title = models.CharField(max_length=100, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    price = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    
    

    def __str__(self):
        return self.title

 

class Beauty(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=100, null=True)
    sub_title = models.CharField(max_length=300, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title

class Access(models.Model):
    image = models.ImageField(null=True, blank=False)
    title = models.CharField(max_length=100, null=True)
    sub_title = models.CharField(max_length=300, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.title

class Store(models.Model):
    user = models.ForeignKey(Customer, models.CASCADE)
    product = models.ForeignKey(Home, models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    avg =  models.FloatField(default=0)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderItem = self.orderitem_set.all()
        for i in orderItem:
            if i.product.digital == False:
                shipping = True
        return shipping

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
    product = models.ForeignKey(Home, on_delete=models.SET_NULL, blank=True,null=True)
    # shoe = models.ForeignKey(Shoe, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    @property
    def get_shoe_total(self):
        shoe_total = self.shoe.price * self.quantity
        return shoe_total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null=True)
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address