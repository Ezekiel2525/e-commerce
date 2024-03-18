from django import forms
from .models import *

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['image', 'product_name', 'description', 'price', 'stock', 'minimum_order']

class UserBillingForm(forms.ModelForm):
    # fullname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class":"input", "placeholder":"Fullname"}))
    class Meta:
        model = Billing
        fields = ['fullname', 'city', 'country', 'zipcode', 'telephone']
    