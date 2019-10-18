from django.db import models

# Create your models here.
class AcaoModelo(models.Model):
    preco = models.CharField(max_length=50)
    mudanca = models.CharField(max_length=50)
    classeMudanca = models.CharField(max_length=50)