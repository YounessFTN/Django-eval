from django.contrib import admin
from .models import Basket

# Enregistrement du modèle Basket
@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')  # Affichez les champs pertinents pour le panier
    search_fields = ('user__username', 'product__name')  # Recherche par nom d'utilisateur et produit
    list_filter = ('user',)  # Filtrer par utilisateur si applicable
