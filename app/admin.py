from django.contrib import admin
from .models import Contact
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'gender', 'info')
    list_display_links = ('id', 'name')
    list_editable = ('phone', 'info')
    list_per_page = 10
    search_fields = ('name', 'email', 'phone', 'gender', 'info',)
    list_filter = ('gender', 'date_added')

# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)