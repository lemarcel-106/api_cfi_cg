from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Article(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    description_courte = models.TextField()
    description_long = CKEditor5Field('Description', config_name='extends')

    def __str__(self):
        return self.titre


class Evenement(models.Model):
    TYPE_CHOICES = [
        ('Gratuit', 'Gratuit'),
        ('Payant', 'Payant'),
    ]

    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='evenements/')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    contions = models.TextField()
    description_courte = models.TextField()
    description_long = CKEditor5Field('Description', config_name='extends')

    def __str__(self):
        return self.titre


class Donation(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse_email = models.EmailField()
    telephone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Adhesion(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse_email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
