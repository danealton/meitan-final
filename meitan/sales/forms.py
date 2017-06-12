from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
		model = Sale
		fields = ('customer_name', 'customer_adress', 'customer_phone', 'customer_email')
