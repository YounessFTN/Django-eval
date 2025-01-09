from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.all()  # Récupère tous les commentaires du produit
    comment_form = CommentForm()

    # Gestion du formulaire de commentaire
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.product = product
            comment.user_name = request.user.username  # Utiliser le nom d'utilisateur de l'utilisateur connecté
            comment.save()
            return redirect('product_detail', product_id=product.id)

    return render(request, 'shop/product_detail.html', {
        'product': product,
        'comments': comments,
        'comment_form': comment_form
    })



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
