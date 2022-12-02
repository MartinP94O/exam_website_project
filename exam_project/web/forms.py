from django import forms

from exam_project.accounts.models import BuyingAddress
from exam_project.web.models import Product


# class ProfileCreateForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'age', 'password',)
#
#
# class ProfileEditForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = '__all__'
#
#
# class ProfileDetailsForm(forms.ModelForm):
#
#     class Meta:
#         model = Profile
#         fields = ()
#
#
# class ProfileDeleteForm(forms.ModelForm):
#
#     def save(self, commit=True):
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Profile
#         fields = ()
#
#
class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class ProductEditForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


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
        disabled = True


class ProductBuyForm(forms.ModelForm):

    class Meta:
        model = BuyingAddress
        fields = '__all__'
