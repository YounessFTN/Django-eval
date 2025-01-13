from django.contrib import admin
from .models import Product, Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')  
    search_fields = ('name', 'description')  
    list_filter = ('created_at', 'price')  
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'product', 'rating', 'created_at') 
    search_fields = ('user_name', 'content')  
    list_filter = ('created_at', 'rating')  

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
