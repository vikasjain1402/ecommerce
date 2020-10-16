from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100,null=True)
    digital=models.BooleanField(default=False)
    image=models.ImageField(null=True,blank=True)
    price=models.FloatField()
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url            



class Order(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    transection_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)+str(self.customer)

    @property
    def get_cart_total(self):
        items=self.order_item_set.all()
        total=0
        for i in items:
            total+=i.quantity*i.product.price
   
        
    @property
    def get_cart_items(self):
        items1=self.order_item_set.all()
        total_items=0
        for j in items1:
            total_items+=j.quantity
        return total_items    

class Order_item(models.Model):
    order=models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)        
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1,null=True)
    date_Added=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total=self.quantity*self.product.price
        return total


class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address =models.CharField(max_length=300,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zip_code=models.CharField(max_length=20,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address