from re import A
from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'nome', 'sobrenome']
    list_display_links = ['user']

admin.site.register(Account, AccountAdmin)


# Register your models here.
