from django.urls import path

from mainapp.views import index, contacts, about, products, product

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:pk>/', product, name='product'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
