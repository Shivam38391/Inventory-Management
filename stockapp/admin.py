from django.contrib import admin
from stockapp.models import Stock
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    list_display = ("__str__", "category", "quantity", "issue_by", "issue_to", )
    list_filter = ( "category", "quantity",)
    
    
admin.site.register(Stock, StockAdmin)