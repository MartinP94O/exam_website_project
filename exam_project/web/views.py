from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from exam_project.web.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm, ProductBuyForm
from exam_project.web.models import Product

UserModel = get_user_model()

# def get_profile():
#     profiles = Profile.objects.all()
#     if profiles:
#         return profiles[0]
#     return None


def show_index(request):
    profile = UserModel

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def catalogue(request):
    profile = UserModel
    products = Product.objects.all()

    context = {
        'products': products,
        'profile': profile,
    }
    return render(request, 'catalogue/catalogue.html', context)


def create_product(request):
    profile = UserModel
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProductCreateForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'product/product-create.html', context)


def product_details(request, pk):
    profile = UserModel
    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
        'profile': profile,
    }
    return render(request, 'product/product-details.html', context)


def product_edit(request, pk):
    profile = UserModel
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product details', pk)
    else:
        form = ProductEditForm(instance=product)
    context = {
        'form': form,
        'product': product,
        'profile': profile,
    }
    return render(request, 'product/product-edit.html', context)


def product_delete(request, pk):

    profile = UserModel
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductDeleteForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProductDeleteForm(instance=product)
    context = {
        'form': form,
        'product': product,
        'profile': profile,
    }
    return render(request, 'product/product-delete.html', context)


def profile_details(request):
    profile = UserModel
    products = Product.objects.all()
    products_price = sum(p.product_price for p in products)
    full_name = ''
    no_picture = True
    if profile.profile_picture:
        no_picture = False

    if profile.first_name:
        full_name = profile.first_name + ' '
    if profile.last_name:
        full_name += profile.last_name

    context = {
        'profile': profile,
        'full_name': full_name,
        'no_picture': no_picture,
        'products_price': products_price,
    }
    return render(request, 'profile/profile-details.html', context)


def product_buy(request, pk):

    profile = UserModel
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductBuyForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            product.delete()
            return redirect('catalogue')
    else:
        form = ProductBuyForm(instance=product)
    context = {
        'form': form,
        'product': product,
        'profile': profile,
    }
    return render(request, 'product/product-buy.html', context)


