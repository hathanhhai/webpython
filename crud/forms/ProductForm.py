from django.core.validators import validate_email, validate_slug, validate_integer
from django import forms
from crud.models.Product import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(required=False, label="Product Name", max_length=100,
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                           }))
    price = forms.CharField(
        required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
    }), required=False)

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
    }), required=False)

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'image',
        ]

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("This is not a valid name")
        else:
            return name

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price.isdigit():
            return price
        else:
            raise forms.ValidationError("Price must is number")
        if not price:
            raise forms.ValidationError("The field price is required")
        else:
            return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise forms.ValidationError("The field description is required")
        else:
            return description

    def clean_image(self):
        image = self.cleaned_data.get("image", False)
        return image
        
