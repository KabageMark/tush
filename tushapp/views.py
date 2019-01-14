from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Cart
from .forms import CartForm
from django.core.exceptions import ObjectDoesNotExist

def shop_page(request):
    tshirts = Product.display_product("tshirt")
    jeans = Product.display_product("jeans")
    Cartform = CartForm()
    return render(request, 'shop.html',{"tshirts":tshirts,"jeans":jeans,"Cartform":Cartform})

def home_page(request):
    return render(request,'index.html')

def cart(request):
    items = Cart.objects.filter(paid='False')
    prices = []
    for item in items:
       price = item.item.price
       prices.append(price)
    print(prices)
    total = sum(prices)
    return render(request,'show-cart.html',{"items":items,"total":total})

def add_to_cart(request,id):
    if request.method == 'POST':
        goodie = Product.objects.get(id=id)
        Cartform = CartForm(request.POST)
        if Cartform.is_valid():
            form = Cartform.save(commit=False)
            form.user = request.user
            form.item = goodie
            form.save()
            return redirect ('cart')
    print('x')

def delete_cart(request,id):
    item = Cart.objects.get(id=id)
    Cart.delete_item(item)
    return redirect('cart')

def empty(request):
    item =  Cart.objects.filter(user=request.user).delete()
    return redirect('cart')

def mobile_checkout(self, product_name, phone_number, currency_code, amount, metadata={},
                        provider_channel=None, callback=None):

        if not validate_phone(phone_number):
            raise ValueError('Invalid amount')

        url = self._make_url('/mobile/checkout/request')
        headers = dict(self._headers)
        headers['Content-Type'] = 'application/json'
        data = {
            'username': self._username,
            'productName': product_name,
            'phoneNumber': phone_number,
            'currencyCode': currency_code,
            'amount': amount,
            'metadata': metadata
        }
        if provider_channel is not None:
                data['providerChannel'] = provider_channel
        data = json.dumps(data)
        return self._make_request(url, 'POST', headers=headers, params=None, data=data, callback=callback)