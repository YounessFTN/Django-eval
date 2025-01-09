from django.contrib import admin
from .models import Product, Comment

# Enregistrer le modèle Product pour qu'il soit modifiable dans l'admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')  # Afficher les colonnes importantes
    search_fields = ('name', 'description')  # Permettre la recherche par nom et description
    list_filter = ('created_at', 'price')  # Filtrer par date et prix

# Enregistrer le modèle Comment pour qu'il soit modifiable dans l'admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'product', 'rating', 'created_at')  # Afficher les colonnes importantes
    search_fields = ('user_name', 'content')  # Permettre la recherche par nom d'utilisateur et contenu
    list_filter = ('created_at', 'rating')  # Filtrer par date et note

# Enregistrer les modèles dans l'admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
