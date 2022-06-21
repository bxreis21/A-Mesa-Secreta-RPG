from django.contrib import admin
from .models import Atributo, Personagen, Ficha


class AtributosAdmin(admin.ModelAdmin):
    list_display = ['id','forca', 'agilidade', 'inteligencia', 'vigor', 'presenca']
    
class PersonagemAdmin(admin.ModelAdmin):
    list_display = ['id','nome','origem', 'nex', 'patente']

class FichaAdmin(admin.ModelAdmin):
    list_display = ['id','mestre','jogador','personagem', 'atributos']

admin.site.register(Atributo, AtributosAdmin)
admin.site.register(Personagen, PersonagemAdmin)
admin.site.register(Ficha, FichaAdmin)

# Register your models here.
