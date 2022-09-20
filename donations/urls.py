from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_donate_page, name='main_page'),
    path('ask_donate/', views.ask_donate, name='ask_donate'),
    path('make_donate/', views.make_donate, name='make_donate'),
    path('list/', views.list, name='list'),
]