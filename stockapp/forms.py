
from django import forms
from stockapp.models import Stock


class StockForm(forms.ModelForm):

    class Meta:

        model = Stock
        fields = ["category", "item_name", "quantity", "receive_quantity", "receive_by"]
