from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Basket

@login_required
def basket_view(request):
    # Récupérer les articles du panier pour l'utilisateur connecté
    basket_items = Basket.objects.filter(user=request.user)

    # Calculer le sous-total pour chaque article et le total
    for item in basket_items:
        item.subtotal = item.product.price * item.quantity

    # Calculer le total du panier
    total = sum(item.subtotal for item in basket_items)

    return render(request, 'basket/basket.html', {
        'basket_items': basket_items,  # Articles du panier avec le sous-total
        'total': total,  # Le total du panier
    })
