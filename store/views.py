from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,completed=False)
        items=order.order_item_set.all()
        context={"order":order}
    else:
        items=[]
        order={'get_cart_total':0,"get_cart_items":0,'shipping':False}
        context={"order":order}
    products=Product.objects.all()
    context['products']=products    
    return render(request,"store.html",context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
    
        order, created =Order.objects.get_or_create(customer=customer,completed=False)
        items=order.order_item_set.all()
        order1={'get_cart_total':order.get_cart_total,"get_cart_items":order.get_cart_items}
    else:
        items=[]
        order1={'get_cart_total':0,"get_cart_items":0,'shipping':False}
    context={"items":items,"order":order1}
  
    return render(request,"cart.html",context=context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer,completed=False)
        items=order.order_item_set.all()

    else:
        items=[]
        order={'get_cart_total':0,"get_cart_items":0,'shipping':False}
    context={"items":items,"order":order}
    return render(request,"checkout.html",context=context)     


def updateitem(request):
   
    data=json.loads(request.body)
    productId=data['productid']
    action=data['action']

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,completed=False)
    order_item,created=Order_item.objects.get_or_create(order=order,product=product)
  
    if action=="add":
        order_item.quantity+=1
    
    elif action=='remove':
        order_item.quantity-=1
    order_item.save()
    if order_item.quantity<=0:
        order_item.delete()  
    
    return JsonResponse("data was added",safe=False)
