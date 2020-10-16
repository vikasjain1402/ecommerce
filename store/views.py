from django.shortcuts import render
from .models import *



def store(request):
    products=Product.objects.all()
    context={"products":products}
    return render(request,"store.html",context)

def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        print("cumtomer",customer)
        order, created =Order.objects.get_or_create(customer=customer,completed=False)
        items=order.order_item_set.all()
    else:
        items=[]
        order={'get_cart_total':0,"get_cart_items":0}
    context={"items":items,"order":order}

    return render(request,"cart.html",context=context)
def checkout(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created =Order.objects.get_or_create(customer=customer,completed=False)
        items=order.order_item_set.all()
    else:
        items=[]
        order={'get_cart_total':0,"get_cart_items":0}
    context={"items":items,"order":order}
    return render(request,"checkout.html",context=context)        
