from django.contrib import admin
from .models import photos, contact
# Register your models here.

admin.site.register(photos)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date')
    
    
    
admin.site.register(contact, PersonAdmin)
