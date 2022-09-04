from itertools import product
from unicodedata import category
from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        Mobile=Product.objects.filter(category='M')
        Laptop=Product.objects.filter(category='L')
        Menbottomwear=Product.objects.filter(category='MB')
        Mentopwear=Product.objects.filter(category='MT')
        Menperfume=Product.objects.filter(category='MP')
        Menshoesandsandals=Product.objects.filter(category='MS')
        Ladiestopwear=Product.objects.filter(category='LT')
        Ladiesbottomwear=Product.objects.filter(category='LB')
        Ladiesperfume=Product.objects.filter(category='LP')
        Ladiesshoesandsandals=Product.objects.filter(category='LS')
        
        return render(request, 'app/home.html', {'Mobile':Mobile,'Laptop':Laptop,
        'Menbottomwear':Menbottomwear,'Mentopwear':Mentopwear,'Menperfume':Menperfume,
        'Menshoesandsandals':Menshoesandsandals,'Ladiestopwear':Ladiestopwear,
        'Ladiesbottomwear':Ladiesbottomwear,'Ladiesperfume':Ladiesperfume,
        'Ladiesshoesandsandals':Ladiesshoesandsandals})



## def product_detail(request):
##  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
    user=request.user
    # product_id=request.GET.get('prod_id')
    # product=Product.objects.get(id=product_id)
    # Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount=40.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.discounted_price)
        return render(request, 'app/addtocart.html',{'carts':cart})

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):    
 return render(request, 'app/orders.html')

def mobile(request, data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data=='Apple' or data=='Samsung' or data=='Realme' or data=='Oppo' \
            or data=='Redmi':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category='M').filter\
            (discounted_price__lt=10000)
    elif data=='above':
        mobiles=Product.objects.filter(category='M').filter\
            (discounted_price__gt=10000)
    return render(request,'app/mobile.html', {'mobiles':mobiles})

def laptop(request, data=None):
    if data==None:
        laptops=Product.objects.filter(category='L')
    elif data=='Apple' or data=='Lenovo' or data=='HP' or data=='Acer' \
            or data=='Dell':
        laptops=Product.objects.filter(category='L').filter(brand=data)
    elif data=='below':
        laptops=Product.objects.filter(category='L').filter\
            (discounted_price__lt=50000)
    elif data=='above':
        laptops=Product.objects.filter(category='L').filter\
            (discounted_price__gt=50000)
    return render(request,'app/laptop.html', {'laptops':laptops})

def customeregistration(request):
    return render(request,'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',
        {'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
          messages.success(request,'Congratulations! Registered Successfully')
          form.save()
        return render(request, 'app/customerregistration.html',
        {'form': form})

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user 
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Hey Congratulations !!! Profile Updated Successfully')
        return render(request,'app/profile.html', {'form':form,'active':'btn-primary'})    