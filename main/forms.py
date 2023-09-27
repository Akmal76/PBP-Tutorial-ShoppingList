from django.forms import ModelForm
from main.models import Product
# from django import forms
# from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description",]

    # Baris baru ini menimpa atau 'override' field user yang otomatis ada dari ModelForm.
    # Gunanya untuk menambahkan atribut tertentu, seperti required=True pada contoh
    # user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)  # NEW 