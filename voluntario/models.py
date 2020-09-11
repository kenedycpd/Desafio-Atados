from django.db import models


class Voluntary(models.Model):
    name = models.CharField('Nome', max_length=50, blank=False)
    last_name = models.CharField('Sobrenome', max_length=50, blank=False)
    neighborhood = models.CharField('Bairro', max_length=200, blank=False)
    city = models.CharField('Cidade', max_length=200, blank=False)

    class Meta:
        verbose_name = 'Voluntario'
        ordering = ['-name']

    def __str__(self):
        return self.name