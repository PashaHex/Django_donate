from django.contrib import admin

# Register your models here.
from donations.models import Office, Item, ItemDescription


class OfficeAdmin(admin.ModelAdmin):
    fields = ['name', 'capacity', 'occupied']
    list_display = ('name', 'capacity', 'occupied')

admin.site.register(Office, OfficeAdmin)

@admin.action(description='Mark selected item as booked')
def make_booked(modeladmin, request, queryset):
    queryset.update(state=True)


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'amount', 'state', 'office']
    list_display = ('name', 'amount', 'state', 'office')

    @admin.action(description='Mark selected item as active')
    def make_active(self, request, queryset):
        queryset.update(state=False)

    actions = [make_booked, make_active, ]

admin.site.register(Item, ItemAdmin)


class ItemDescriptionAdmin(admin.ModelAdmin):
    fields = ['estimate', 'comment', 'target']
    list_display = ('estimate', )

admin.site.register(ItemDescription, ItemDescriptionAdmin)