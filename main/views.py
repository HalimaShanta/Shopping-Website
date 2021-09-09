from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Avg
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder



# Create your views here.
def home(request):
    data = cartData(request)
    cartItems = data['cartItems']
    review = Store.objects.all()
    review_avg = review.aggregate(avg=Avg('rate'))
    review_count = review.count()
    print(review_avg)
    
    
    img = Home.objects.all()
    context = {'img':img, 'cartItems':cartItems,'review':review,'review_avg':review_avg,
    'review_count':review_count}
    return render(request, 'home.html', context)



def store(request,id):
    product = Home.objects.filter(id=id)
    productreview = Home.objects.get(id=id)
    review = Store.objects.filter(product=productreview)
    review_avg = review.aggregate(avg_rate=Avg('rate'))
    review_count =review.count()
    avg = review_avg['avg_rate']
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
     

    # print(review_avg)

    # print(review)
    
    context = {'product':product,'review':review,'review_avg':review_avg,'review_count':review_count,'cartItems':cartItems,
    'order':order,'items':items,'avg':review_avg}
    return render(request, 'store.html', context)


def review(request):
    if request.method == "GET":
        prod_id = request.GET.get('prod_id')
        product = Home.objects.get(id=prod_id)
        comment = request.GET.get('comment')
        rate = request.GET.get('rate')
        # avg = request.GET.get('avg_rate')
        avg_rate = request.GET.get('avg_rate')
        user = request.user.customer

        # reviews = Store.objects.filter(product=self).aggregate(average=Avg('rate'))
        # rev = Store.objects.annonate(avg_rating=Avg('rate')).order_by('-avg_rating')
    
    Store(user=user,product=product,comment=comment,rate=rate,avg=avg_rate).save()
    return redirect('store',id=prod_id)
def fashion(request):
    product = Home.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context={'product': product,'cartItems':cartItems,'order':order,'items':items}
    return render(request, 'fashion.html',context)

def beauty(request):
    product = Beauty.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context={'product': product,'cartItems':cartItems,'order':order,'items':items}
    return render(request, 'beauty.html',context)

def accesories(request):
    product = Access.objects.all()
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context={'product': product,'cartItems':cartItems,'order':order,'items':items}
    return render(request, 'accesories.html',context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']



    # data = cookieCart(request)
    
        

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'chekout.html', context)
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Home.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
       orderItem.delete()

    return JsonResponse('Item was added', safe=False)
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
    else:
        customer , order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
        

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            )

    return JsonResponse('Payment Complete', safe=False)