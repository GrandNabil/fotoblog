from django.db import models
from django.contrib.auth.models import AbstractUser # utilisation d'un modèle prédéfini dans django

class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUSCRIBER = 'SUSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUSCRIBER, 'Abonné'),
                    )
    profile_photo = models.ImageField(verbose_name='Photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

