from django.db.models.expressions import result
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

author = {
        'Имя': 'Иван',
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
        "телефон": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity":5},
    {"id": 2, "name": "Кожанная куртка", "quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity":12},
    {"id": 7, "name": "Картофель фри", "quantity":0},
    {"id": 8, "name": "Кепка", "quantity":124},
]


def home(request):
    # text = """
    # <h1>"Извучаем django"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # """
    # return HttpResponse(text)
    context = {
        "name": "Иванов Петр Семенович",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""
        Имя: {author["Имя"]}<br>
        Отчество: {author['Отчество']}<br>
        Фамилия: {author['Фамилия']}<br>
        телефон: {author['телефон']}<br>
        email: {author['email']}<br>
        """
    return HttpResponse(text)

def get_item(request, item_id: int):
    """ По указанному id возвращает элемент из списка """
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2> Имя: {item['name']} </h2>
            <p> Колличество: {item['quantity']} </p>
            <p> <a href='/items'> back to items list </a>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id={item_id} not found')


def get_items(request):

    context = {"items": items}
    return render(request, "items_list.html", context)

