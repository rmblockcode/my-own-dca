from django.db import models

class DCAParameter(models.Model):
    exchange_id = models.CharField(
        'Exchange ID', max_length=30,
        unique=True
    )
    exchange_description = models.CharField(
        'Nombre del Exchange', max_length=30
    )
    api_key = models.CharField(
        'API Key', max_length=250
    )
    secret = models.CharField(
        'Secret', max_length=250
    )
    password = models.CharField(
        'Contraseña (Requerida por algunos exchanges)',
        max_length=250,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.exchange_id} - {self.exchange_description}'
