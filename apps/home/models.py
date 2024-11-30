# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Imoveis(models.Model):
    codlote = models.CharField(verbose_name='Codlote', max_length=11)
    inscant = models.CharField(verbose_name='Inscant', max_length=11)
    parcelament = models.CharField(verbose_name='Parcelament', max_length=100)
    proprietar = models.CharField(verbose_name='Proprietar', max_length=100)
    patrimonio = models.CharField(verbose_name='Patrimonio', max_length=100)
    taxacao = models.CharField(verbose_name='Taxação', max_length=100)
    descricao = models.CharField(verbose_name='Descrição', max_length=100)  # Corrigi 'DESRIÇAOT' para 'descricao'
    usoimovel = models.CharField(verbose_name='Uso do Imóvel', max_length=100)
    setorcalcu = models.CharField(verbose_name='Setor Cálculo', max_length=100)

    def __str__(self):
        return self.inscant
