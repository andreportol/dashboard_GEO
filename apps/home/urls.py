# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import ImoveisFilter


urlpatterns = [

    # The home page
    path('', views.index, name='home'),  
    
    # My urls.py
    path('pesquisar/', ImoveisFilter.as_view(), name='pesquisar_imoveis'),
]
