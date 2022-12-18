from django.urls import path

from exam_project.web.views import show_index, catalogue, create_product, product_details, product_edit, \
    product_delete, product_buy, contact_us, edit_contact_us

urlpatterns = (
    path('', show_index, name='show index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('contacts/', contact_us, name='contact us'),
    path('contacts/edit/', edit_contact_us, name='edit contact us'),
    path('product/create/', create_product, name='create product'),
    path('product/<int:pk>/details/', product_details, name='product details'),
    path('product/<int:pk>/edit/', product_edit, name='product edit'),
    path('product/<int:pk>/delete/', product_delete, name='product delete'),
    path('product/<int:pk>/buy/', product_buy, name='product buy'),

)
