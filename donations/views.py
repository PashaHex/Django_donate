import json

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render


def main_donate_page(request):
    context = {
        'ask_donate': reverse('ask_donate'),
        'make_donate': reverse('make_donate')
    }
    return render(request, 'main.html', context)


def list(request):
    context = {}
    with open('items.json', 'r') as items:
        context['items'] = json.load(items)
    return render(request, 'list.html', context)


def ask_donate(request):
    item = None
    with open('items.json', 'r') as items:
        items_list = json.load(items)

    if items_list and request.method == 'POST':
        item = items_list.pop()

        with open('items.json', 'w') as items:
            json.dump(items_list, items)
    return render(request, 'ask_donate_complete.html', {'item': item})

def make_donate(request):
    with open('items.json', 'r') as items:
        items_list = json.load(items)
        item = items_list.append(
            {'name': request.POST['donation_item'], 'amount': request.POST['donation_amount']}
        )
    with open('items.json', 'w') as items:
        json.dump(items_list, items)
    return render(
        request,
        'make_donate_complete.html',
        {'main_page': reverse('main_page')}
    )