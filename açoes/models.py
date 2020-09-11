from django.db import models
from voluntario.models import Voluntary

class Actions(models.Model):
    name_action = models.CharField('Nome da Ação', max_length=300, blank=False)
    institution_organizing = models.CharField('Nome da Instituição', max_length=300, blank=False)
    city = models.CharField('Cidade', max_length=200, blank=False)
    neighborhood = models.CharField('Bairro', max_length=200, blank=False)
    address = models.CharField('Endereço', max_length=200, blank=False)
    description = models.TextField('Descrição', blank=False)
    incluir_voluntario = models.ForeignKey(Voluntary, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Açoes'
        ordering = ['name_action']