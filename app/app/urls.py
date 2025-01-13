from shop import views as shop_views
from basket import views as basket_views  # Import des vues pour le panier
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Administration
    path('admin/', admin.site.urls),

    # Produits
    path('products/', shop_views.product_list, name='product_list'),
    path('product/<int:product_id>/', shop_views.product_detail, name='product_detail'),
    path('product/', shop_views.product_list, name='product_list_redirect'),

    # Utilisateurs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', shop_views.signup, name='signup'),

    # Panier
    path('basket/', basket_views.basket_view, name='basket_view'),
]

# Gestion des fichiers médias en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
