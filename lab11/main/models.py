from django.db import models

# Create your models here.


class Funcs(models.Model):
    func = models.DecimalField(decimal_places=3, max_digits=10)
