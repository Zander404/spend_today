from django import forms
from .models import Category, Nota


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class NotaForm(forms.ModelForm):

    def clean_value(self):
        value = self.cleaned_data['value']

        if value < 0:
            raise forms.ValidationError("O valor deve ser positivo!")

        return value

    class Meta:
        model = Nota
        fields = '__all__'
