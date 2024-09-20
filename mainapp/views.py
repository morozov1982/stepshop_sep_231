from django.shortcuts import render


def get_menu_links(current='mainapp:index'):
    return [
        {'href': 'mainapp:index', 'name': 'Главная', 'active': current},
        {'href': 'mainapp:products', 'name': 'Продукты', 'active': current},
        {'href': 'mainapp:about', 'name': 'О&nbsp;нас', 'active': current},
        {'href': 'mainapp:contacts', 'name': 'Контакты', 'active': current},
    ]

def index(request):
    title = 'главная'

    context = {
        'title': title,
        'menu_links': get_menu_links(),
    }
    return render(request, 'index.html', context)


def products(request):
    title = 'товары'
    context = {
        'title': title,
        'menu_links': get_menu_links('mainapp:products'),
    }
    return render(request, 'products.html', context)


def about(request):
    title = 'о нас'
    context = {
        'title': title,
        'menu_links': get_menu_links('mainapp:about'),
    }
    return render(request, 'about.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
        'menu_links': get_menu_links('mainapp:contacts'),
    }
    return render(request, 'contacts.html', context)
