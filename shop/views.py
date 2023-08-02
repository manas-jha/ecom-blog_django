from django.shortcuts import render
from django.http import HttpResponse
from .models import product, contact, order, orderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt   #for paytm integration excempt csrf
# from paytm import Checksum
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

# Create your views here.



def index(request):
    allprods = []
    catprod = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, nSlides, range(1, nSlides)])

    params = {'allprod':allprods}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    if query in item.desc or item.product_name or query in item.category:
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprods = []
    catprod = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prodtemp = product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0:
            allprods.append([prod, nSlides, range(1, nSlides)])

    params = {'allprod':allprods}
    return render(request, 'shop/index.html', params)




def about(request):
    return render(request, 'shop/about.html')


def contact_info(request):
    thank = False
    if request.method == "POST":
        fname = request.POST.get('fname','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contacts = contact(name=fname, email=email, phone=phone, desc=desc)
        contacts.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            orders = order.objects.filter(order_id=orderId, email=email)
            if len(orders)>0:
                update = orderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timeStamp})
                    response = json.dumps([updates,orders[0].items_json], default=str)
                return HttpResponse(response)
            else: 
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')



def prodView(request, myid):
    prodv = product.objects.filter(id = myid)
    return render(request, 'shop/productView.html', {'product':prodv[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('items_json','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        print(amount)
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        orders = order(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone, amount=0)
        # orders.save()

        order_id_track = orders.order_id
        update = orderUpdate(order_id=order_id_track, update_desc="Order placed")
        # update.save()

        thank = True
        id = orders.order_id
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
        # Request paytm to transfer the amount to my account after payment by user
        param_dict = {
            'MID':'WorldP64425807474247',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://http://127.0.0.1:8000/shop/handlerequest/',
        }
        # param_dict['CHECKSUMHASH']= Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {"param_dict":param_dict})



    return render(request, 'shop/checkout.html')

# paytm integration
@csrf_exempt
def handlerequest(request):
    return HttpResponse('')