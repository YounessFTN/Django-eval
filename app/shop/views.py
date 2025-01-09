from django.shortcuts import render, get_object_or_404
from .models import Product, Comment

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    comments = Comment.objects.filter(product=product)
    
    for comment in comments:
        # Calcul des étoiles pleines et vides
        comment.full_stars = comment.rating
        comment.empty_stars = 5 - comment.rating

    return render(request, 'shop/product_detail.html', {'product': product, 'comments': comments})