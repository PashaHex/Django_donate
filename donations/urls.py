from django.urls import path, re_path, include
from . import views


app_name = 'donations'

urlpatterns = [
    path('', views.main_donate_page, name='main_page'),
    path('set_office', views.set_session_office, name='set_session_office'),
    path('offices/create', views.CreateOfficesView.as_view(), name='offices_create'),
    path('offices', views.OfficesView.as_view(), name='offices'),
    path('ask_donate/', views.ask_donate, name='ask_donate'),
    path('make_donate/)', views.make_donate, name='make_donate'),
    path('list/', views.list, name='list'),
    re_path('donate/(?P<id>[\d-]+)/comment', views.donate_comment, name='donate_comment'),
]




















