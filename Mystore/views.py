from django.shortcuts import render,redirect
from .models import Product
from .forms import Addition


def productlist(request):
    data=Product.objects.all()
    return render(request,'Mystore/productlist.html',{'products':data})

def displayProducts (request,name):
    pro=Product.objects.filter(category__name=name)
    return render(request,'Mystore/display.html',{'products':pro})


def Home(request):
    latestproduct=Product.objects.order_by('-created_at')[:4]
    return render(request,'Mystore/Home.html',{'products':latestproduct})


def search(request):
    cases=request.GET.get('word')

    if cases:
        products=Product.objects.filter(name__icontains=cases)

    else:
        products=Product.objects.none()

    return render(request,'Mystore/search.html',{'products':products,'cases':cases})       

def addproduct(request):
    if request.method == 'POST':
        y = Addition(request.POST,request.FILES)
        if y.is_valid():
            y.save()
            return redirect('Home')
    else:
        y = Addition()
    return render(request, 'Mystore/addproduct.html', {'form': y})


def Product_Details(request,id):
    details=Product.objects.get(id=id)
    return render(request,'Mystore/pro_details.html',{'details':details})

def Update_product(request,id):
    x=Product.objects.get(id=id)
    if request.method =='POST':
        data = Addition(request.POST,request.FILES,instance=x)
        if data.is_valid():
            data.save() 
            return redirect('Home')       
    else:
        data = Addition(instance=x)
    return render(request, 'Mystore/addproduct.html', {'form': data})

def delete_product(request,id):
    product=Product.objects.get(id=id)
    if request.method =='POST':
        product.delete()
        return redirect('Home')
    return render(request, 'Mystore/addproduct.html', {'product': product})
    