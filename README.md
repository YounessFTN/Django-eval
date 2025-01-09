# Django Eval Project

Ce projet est une application Django pour afficher une liste de produits avec des détails et des commentaires.

## Prérequis

- Python 3.12
- Django 5.1.4

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/django-eval.git
   cd django-eval
   ```

2. Créez et activez un environnement virtuel :

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations de la base de données :

   ```bash
   python manage.py migrate
   ```

5. Créez un superutilisateur pour accéder à l'admin :

   ```bash
   python manage.py createsuperuser
   ```

6. Démarrez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

## Utilisation

- Accédez à l'interface d'administration à l'adresse `http://127.0.0.1:8000/admin/` pour ajouter des produits.
- Accédez à la liste des produits à l'adresse `http://127.0.0.1:8000/products/`.

## Structure du projet

- [app](http://_vscodecontentref_/1): Contient les fichiers de configuration du projet Django.
- `shop/`: Contient l'application principale avec les modèles, vues, templates et fichiers statiques.
- `media/`: Contient les fichiers médias téléchargés par les utilisateurs.

## Configuration

### Fichiers statiques et médias

Assurez-vous que les paramètres pour les fichiers statiques et médias sont correctement configurés dans `settings.py` :

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (Uploaded by users)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```
