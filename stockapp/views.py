from django.shortcuts import render

# Create your views here.

def add_stock(request):
    return render(request, "stockapp/add_stock.html")