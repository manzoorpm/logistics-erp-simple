import email
from django.forms import ModelForm
from .models import Order, Warehouse, Product
from django import forms

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class WarehouseForm(ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Warehouse Name", "maxlength": "256", "name": "name", "id":"name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Warehouse Email", "maxlength": "256", "name": "email", "id":"email"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Warehouse Phone", "maxlength": "256", "name": "phone", "id":"phone"}))
	place = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Warehouse City", "maxlength": "256", "name": "place", "id":"place"}))

	class Meta:
		model = Warehouse
		fields = ['name', 'phone', 'email', 'place']

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'