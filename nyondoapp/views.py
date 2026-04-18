from django.shortcuts import render

# Create your views here.
def sales(request):
    return render(request,'sales.html')
def credit(request):
    return render(request,'credit.html')
def login(request):
    return render(request, 'login.html')
def dashboardsales(request):
    return render(request,'dashboardsales.html')
def index(request):
    return render(request,'index.html')
def product(request):
    return render(request,'product.html')
def newproduct(request):
    return render(request, 'newproduct.html')
def sales2(request):
    return render(request, 'sales2.html')