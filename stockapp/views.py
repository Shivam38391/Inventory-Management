from django.shortcuts import render
from django.views import View

from stockapp.models import Stock
from .forms import StockForm
# Create your views here.

def add_stock(request):
    
    # if request.method == 'POST':
        
    
    return render(request, "stockapp/add_stock.html")


def list_stock(request):
    
    stocks = Stock.objects.all()
    
    context = {
        "stocks":stocks,
    }
    
    return render(request, "stockapp/list_stock.html", context)




class ListView(View):
    template_name= "stockapp/stocktable.html"
    
    model = Stock
    def get(self, request, *args, **kwargs):
        
        stocks = self.model.objects.all()
        
        context = {
            "stocks": stocks,
        }
        return render(request,self.template_name, context)