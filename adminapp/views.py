from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404

from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product


def user_create(request):
    pass


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_create.html'
    success_url = reverse_lazy('admin_staff:users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context['title'] = 'Админка | Пользователи | Создать'
        return context


def users(request):
    title = 'Админка | Пользователи'
    user_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                '-is_staff', 'username')
    context = {
        'title': title,
        'objects': user_list,
    }

    return render(request, 'adminapp/users.html', context)


class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data()
        context['title'] = 'Админка | Пользователи'
        return context

    def get_queryset(self):
        return ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                '-is_staff', 'username')


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



