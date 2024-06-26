from django.forms import ModelForm, BooleanField
from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("owner", )


    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        exception_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in exception_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово: {word}!!!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        exception_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in exception_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово: {word}!!!')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("description", "category", "is_published",)


class VersionForm(StyleFormMixin, ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['version_indicator'].widget.attrs['class'] = ''

    class Meta:
        model = Version
        fields = "__all__"
