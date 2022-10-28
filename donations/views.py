import json

from django.http import HttpResponse
from django.views import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView

from Django_projects.forms import DonateCommentForm, ItemForm, OfficeForm
from donations.models import Item, ItemDescription, Office


def main_donate_page(request, item_form=None):
    context = {
        'office_form': OfficeForm(data={'office': request.session['office_id']}),
        'ask_donate': reverse('donations:ask_donate'),
        'make_donate': reverse('donations:make_donate'),
        'item_form': item_form if item_form else ItemForm(),
    }
    return render(request, 'main.html', context)


def set_session_office(request):
    form = OfficeForm(data=request.POST)
    if form.is_valid():
        request.session['office_id'] = form.cleaned_data['office'].id
    return redirect('donations:main_page')


def donate_comment(request, **kwargs):
    context = {}
    if request.method == 'POST':
        form = DonateCommentForm(request.POST)
        if form.is_valid():
            ItemDescription.objects.create(
                estimate=form.cleaned_data['estimate'],
                comment=form.cleaned_data['comment'],
                target_id=kwargs['id']
            )
            return redirect('donations:list')
        context['form'] = form
    else:
        context['form'] = DonateCommentForm()
    return render(request, 'donate_comment.html', context)


def list(request):
    context = {'items': Item.objects.all().prefetch_related('itemdescription_set')}
    return render(request, 'list.html', context)


def ask_donate(request):
    item = Item.objects.order_by('id').filter(state=False).first()
    if item:
        item.state = True
        item.save()

    return render(request, 'ask_donate_complete.html', {'item': item})

def make_donate(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        item.office_id = request.session['office_id']
        item.save()
        form.save_m2m()
    else:
        return main_donate_page(request, form)

    return render(
        request,
        'make_donate_complete.html',
        {'item':item, 'main_page': reverse('donations:main_page')}
    )


class OfficesView(ListView):
    template_name = "offices_list.html"
    model = Office
    context_object_name = 'offices'

    paginate_by = 3


class CreateOfficesView(CreateView):
    template_name = "create_offices.html"
    model = Office
    fields = ('name', 'capacity', 'occupied')
    success_url = reverse_lazy('donations:offices')














