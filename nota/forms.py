from django import forms
from .models import Category, Nota


class \
        CategoryForm(forms.ModelForm):
    class Meta:
         model = Category
         fields = '__all__'


class Nota(forms.ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'

