from django.db import models

# Create your models here.
class Still(models.Model):
    name = models.CharField("Nome", max_length=255)
    link = models.TextField("Link do Vídeo", null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    datasheet = models.TextField("Ficha Técnica", null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Still'
        verbose_name_plural = 'Stills'

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField("Nome", max_length=255)
    logo = models.ImageField("Logo", upload_to='clientsicons/%Y/%m/%d/', max_length=255, null=True, blank=True)
    created_at = models.DateTimeField("Criado em", auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
        