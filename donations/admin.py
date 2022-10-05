from django.contrib import admin

# Register your models here.
from donations.models import Office, Item

class OfficeAdmin(admin.ModelAdmin):
    fields = ['name', 'capacity', 'occupied']
    list_display = ('name', 'capacity', 'occupied')

admin.site.register(Office, OfficeAdmin)


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'amount', 'state', 'office']
    list_display = ('name', 'amount', 'state', 'office')

admin.site.register(Item, ItemAdmin)