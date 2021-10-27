from django.contrib import admin
from .models import Lanche,Pedido,Ingrediente

# Register your models here.
class detLanche(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'tipo', 'imagem')
    list_display_links = ('nome',)
    search_fields = ('nome',)

class detPedido(admin.ModelAdmin):
    list_display = ('id', 'nomeCliente', 'data', 'fk_Lanche')
    list_display_links = ('nomeCliente',)
    search_fields = ('nomeCliente',)

class detIngrediente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'valor', 'quantidade')
    list_display_links = ('nome',)
    search_fields = ('nome',)


admin.site.register(Ingrediente, detIngrediente)
admin.site.register(Pedido, detPedido)
admin.site.register(Lanche, detLanche)