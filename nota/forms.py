from django import forms
from .models import Category, Nota


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class NotaForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input'}))
    description = forms.CharField(widget=forms.Textarea({'class': 'form-control textarea'}))
    value = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control input'}))
    datetime = forms.DateField(widget=forms.DateInput(attrs={"type": "date", 'class': 'flex select'}))
    category = forms.ModelChoiceField( widget=forms.Select(attrs={"class": 'flex select'}), queryset=Category.objects.all())

    def clean_value(self):
        value = self.cleaned_data['value']

        if value < 0:
            raise forms.ValidationError("O valor deve ser positivo!")

        return value

    class Meta:
        model = Nota
        fields = '__all__'
