# from MainApp.models import Item
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render

author = {
        'Имя': 'Иван',
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
        "телефон": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }

# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity":5},
#     {"id": 2, "name": "Кожанная куртка", "quantity":2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
#     {"id": 7, "name": "Картофель фри", "quantity":0},
#     {"id": 8, "name": "Кепка", "quantity":124},
# ]


def home(request):
    context = {
        "name": "Иванов Петр Семенович",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        'name': 'Иван',
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }
    return render(request, "about.html", {"author": author})



def get_item(request, item_id: int):
    """ По указанному id возвращает элемент из списка """
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return HttpResponseNotFound(f'Item with id={item_id} not found')
    else:
        context = {"item": item}
        return  render(request, "item_page.html", context)



def get_items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)

