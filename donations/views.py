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
    with open('items.json', 'r') as items:
        items_list = json.load(items)

    if not items_list:
        return HttpResponse(
            f'''
                        <html>
                          <body>
                            <h3> We have nothing for you </h3>
                            <a href='{reverse("main_page")}'>Back to main page</a>
                          </body>
                        </html>
                        '''
        )
    item = items_list.pop()

    with open('items.json', 'w') as items:
        json.dump(items_list, items)
    return HttpResponse(
        f'''
                <html>
                  <body>
                    <h3> Please take it </h3>
                    {item['name']} {item['amount']}
                    <a href='{reverse("main_page")}'>Back to main page</a>
                  </body>
                </html>
                '''
    )

def make_donate(request):
    with open('items.json', 'r') as items:
        items_list = json.load(items)
        item = items_list.append(
            {'name': request.POST['donation_item'], 'amount': request.POST['donation_amount']}
        )
    with open('items.json', 'w') as items:
        json.dump(items_list, items)
    return HttpResponse(
        f'''
                    <html>
                      <body>
                        <h3> Thanck you </h3>
                        <a href='{reverse("main_page")}'>Back to main page</a>
                      </body>
                    </html>
                    '''
    )