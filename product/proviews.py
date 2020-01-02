from django.shortcuts import render
from product.models import Product

def product_manage(request):
    username=request.session.get("user","")
    product_list=Product.objects.all()
    return render(request,"product_manage.html",{"user":username,"products":product_list})

# Create your views here.
