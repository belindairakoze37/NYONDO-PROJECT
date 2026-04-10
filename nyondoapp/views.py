from django.shortcuts import render

# Create your views here.
def sales(request):
    return render(request,'sales.html')
def credit(request):
    return render(request,'credit.html')
def login(request):
    return render(request, 'login.html')