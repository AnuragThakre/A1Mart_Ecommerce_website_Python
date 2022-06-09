from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
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



def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
