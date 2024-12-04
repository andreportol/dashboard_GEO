# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import PesquisarDados, MostrarDados

urlpatterns = [

    # The home page
    path('', views.index, name='home'),  
    
    # MINHAS urls.py
    path('pesquisar/', PesquisarDados.as_view(), name='pesquisar_dados'), # botao pesquisar -> sidebar do dashboard
    path('dados_filtrados/', MostrarDados.as_view(), name='dados_filtrados'), # botao consultar -> dados filtrados na tabela
    path('mais_dados_filtrados/<int:pk>/', MostrarDados.as_view(), name='mais_dados_filtrados'), # botao ver -> mais dados da tabela  
    #path('atualizar_valor_iptu_estimado/', atualizar_valor_iptu_estimado(), name='atualizar_valor_iptu_estimado'),
]
