from django import forms

from exam_project.web.models import Product, BuyingAddress, ShopInfo


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_type': 'Type',
            'product_model': 'Model',
            'product_year': 'Year of production',
            'product_image': 'Image URL',
            'product_price': 'Price',
        }


class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_type': 'Type',
            'product_model': 'Model',
            'product_year': 'Year of production',
            'product_image': 'Image URL',
            'product_price': 'Price',
        }


class ProductDetailsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ()


class ProductDeleteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_price'].disabled = True
        self.fields['product_year'].disabled = True
        self.fields['product_type'].disabled = True
        self.fields['product_model'].disabled = True
        self.fields['product_image'].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_type': 'Type',
            'product_model': 'Model',
            'product_year': 'Year of production',
            'product_image': 'Image URL',
            'product_price': 'Price',
        }
        disabled = True


class ProductBuyForm(forms.ModelForm):
    class Meta:
        model = BuyingAddress
        fields = '__all__'


class ContactInfoEdit(forms.ModelForm):

    class Meta:
        model = ShopInfo
        fields = '__all__'
        labels = {
            'shop_name': 'Store name',
            'shop_address': 'Address',
            'shop_email': 'Email'
        }
