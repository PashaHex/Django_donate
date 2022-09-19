import json
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render


def main_donate_page(request):
    # ask_donate = reverse('ask_donate')
    return HttpResponse(
        f'''
        <html>
          <body>
            <h3> Ask donation form </h3>
            <form method='post' action='{reverse("ask_donate")}'>
            <button type='submit'>Click for ask donate</button>
            </form>
            <h3> Make donation form </h3>
            <form method='post' action='make_donate/'>
            <label> name </label>
            <input type='text' name='name'>
            <label> amount </label>
            <input type='number' name='amount'>
            <button type='submit'>Click for make donate</button>
            </form>
          </body>
        </html>
        '''
    )


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
            {'name': request.POST['name'], 'amount': request.POST['amount']}
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