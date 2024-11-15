from django.shortcuts import render, get_object_or_404

from authapp.models import ShopUser
from mainapp.models import Category, Product


def user_create(request):
    pass


def users(request):
    title = 'Админка | Пользователи'
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                '-is_staff', 'username')
    context = {
        'title': title,
        'objects': user_list,
    }

    return render(request, 'adminapp/users.html', context)


def user_update():
    pass


def user_delete():
    pass


def category_create():
    pass


def categories(request):
    title = 'Админка | Категории'
    categories_list = Category.objects.all()
    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


def category_update():
    pass


def category_delete():
    pass


def product_create():
    pass


def products(request, pk):
    title = 'Админка | Продукты'
    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')
    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


def product_read():
    pass


def product_update():
    pass


def product_delete():
    pass



