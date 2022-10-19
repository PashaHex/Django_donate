import json

from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect

from Django_projects.forms import DonateCommentForm
from donations.models import Item


def main_donate_page(request):
    context = {
        'ask_donate': reverse('donations:ask_donate'),
        'make_donate': reverse('donations:make_donate')
    }
    return render(request, 'main.html', context)

def donate_comment(request, **kwargs):
    context = {}
    if request.method == 'POST':
        form = DonateCommentForm(request.POST)
        if form.is_valid():
            return redirect('donations:list')
        context['form'] = form
    else:
        context['form'] = DonateCommentForm()
    return render(request, 'donate_comment.html', context)


def list(request):
    context = {'items': Item.objects.all()}
    # with open('items.json', 'r') as items:
    #     context['items'] = json.load(items)
    return render(request, 'list.html', context)


def ask_donate(request):
    item = Item.objects.order_by('id').filter(state=False).first()
    if item:
        item.state = True
        item.save()

    return render(request, 'ask_donate_complete.html', {'item': item})

def make_donate(request):
    Item.objects.create(
        name=request.POST['donation_item'],
        amount=request.POST['donation_amount']
    )

    return render(
        request,
        'make_donate_complete.html',
        {'main_page': reverse('donations:main_page')}
    )

















