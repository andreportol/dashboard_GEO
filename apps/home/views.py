# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F, Sum, Count
import locale
from .models import Tiqimo
from django.core.cache import cache
from django.db.models import Q


# Configura o locale para o padrão brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


@login_required(login_url="/login/")


def index(request):
    # Tente obter os valores do cache
    cache_key = "index_aggregated_data"
    cached_data = cache.get(cache_key)

    if not cached_data:
        # Calcula os valores se não estiverem em cache
        dados_agrupados = Tiqimo.objects.aggregate(
            total_imoveis=Count('id'),
            valor_IPTU_estimado=Sum('valor_iptu_estimado'),
            lotes_distintos=Count('codelote', distinct=True),
            lotes_com_area_zero=Count('codelote', filter=Q(areaedificimovel=0)),
        )

        # Calcula os tipos de taxação e suas quantidades
        tipos_taxacao = list(Tiqimo.objects.values('taxacao').annotate(quantidade=Count('taxacao')))
        
        # Extraia rótulos e valores de 'taxacao'
        taxacao_labels = [item['taxacao'] for item in tipos_taxacao]
        taxacao_data = [item['quantidade'] for item in tipos_taxacao]

        # Calcula os tipos de patrimonio e suas quantidades
        tipos_patrimonio = list(Tiqimo.objects.values('patrimonio').annotate(quantidade=Count('patrimonio')))
        
        # Extrai rótulos e valores de 'patrimonio'
        patrimonio_labels = [item['patrimonio'] for item in tipos_patrimonio]
        patrimonio_data = [item['quantidade'] for item in tipos_patrimonio]
        
        # Armazena no cache por 10 minutos
        cached_data = {
            'dados_agrupados': dados_agrupados, 
            'tipos_taxacao': tipos_taxacao,
            'tipos_patrimonio': tipos_patrimonio,
        }
        cache.set(cache_key, cached_data, 600)
    else:
        # Recupera os dados do cache
        dados_agrupados = cached_data['dados_agrupados']
        tipos_taxacao = cached_data['tipos_taxacao']
        tipos_patrimonio = cached_data['tipos_patrimonio']

        # Extraímos novamente os rótulos e dados de taxação, caso o cache já tenha sido recuperado
        taxacao_labels = [item['taxacao'] for item in tipos_taxacao]
        taxacao_data = [item['quantidade'] for item in tipos_taxacao]

        # Extrai rótulos e valores de 'patrimonio'
        patrimonio_labels = [item['patrimonio'] for item in tipos_patrimonio]
        patrimonio_data = [item['quantidade'] for item in tipos_patrimonio]

    # Formatação dos resultados
    valor_IPTU_estimado_formatado = locale.format_string('%.2f', dados_agrupados['valor_IPTU_estimado'] or 0, grouping=True)
    lotes_distintos_formatado = locale.format_string('%.0f', dados_agrupados['lotes_distintos'], grouping=True)
    lotes_com_area_zero_formatado = locale.format_string('%.0f', dados_agrupados['lotes_com_area_zero'], grouping=True)

    context = {
        'segment': 'index',
        'Total_imoveis': dados_agrupados['total_imoveis'],
        'valor_iptu_estimado': valor_IPTU_estimado_formatado,
        'total_lotes_distintos': dados_agrupados['lotes_distintos'],  # Valor bruto
        'lotes_com_area_zero': dados_agrupados['lotes_com_area_zero'],  # Valor bruto
        'total_lotes_distintos_formatado': lotes_distintos_formatado,  # Para exibição
        'lotes_com_area_zero_formatado': lotes_com_area_zero_formatado,  # Para exibição
        'taxacao_labels': taxacao_labels,
        'taxacao_data': taxacao_data,
        'patrimonio_labels': patrimonio_labels,
        'patrimonio_data': patrimonio_data,
    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# Minhas classes e métodos

from .models import Tiqimo
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
import unicodedata


def normalizar_texto(texto):
        # Normaliza o texto para decompor os caracteres acentuados
        #Decompõe caracteres como "á" em "a" + um código especial que representa o acento.
        texto_normalizado = unicodedata.normalize('NFKD', texto)
        # Remove os acentos mantendo apenas os caracteres base
        texto_sem_acento = ''.join([char for char in texto_normalizado if not unicodedata.combining(char)])
        # Substitui "ç" por "c"
        texto_sem_acento = texto_sem_acento.replace('ç', 'c').replace('Ç', 'C')
        return texto_sem_acento
'''
    Método para atualizar o atributo desnormalizado "valor_iptu_estimado";
    É necessário chamá-lo toda vez que a tabela for atualizada, pois não existe o campo "valor_iptu_estimado" na tabela original;
    Durante a atualização dos dados da tabela, será necessário recarregar os dados do campo "valor_iptu_estimado";

def atualizar_valor_iptu_estimado():
    # regarregando os dados na coluna valor_iptu_estimado
    dados = Tiqimo.objects.all()
    for dado in dados:
        dado.valor_iptu_estimado = dado.avaliacao * (dado.aliquota / 100)
        dado.save()

'''
# classe utilizada para listar e pesquisar os dados
class PesquisarDados(View):
    template_name = 'home/pesquisa_imoveis.html'

    def get(self, request, *args, **kwargs):
        # Renderizar o template inicial sem dados ou com filtros padrão
        return render(request, self.template_name, {'imoveis': []})   

    def post(self, request, *args, **kwargs):
        # Capturar os filtros enviados no formulário através do botao consultar
        proprietario = request.POST.get('proprietario', '').strip()
        parcelamento = request.POST.get('parcelamento', '').strip()
        patrimonio = request.POST.get('patrimonio', '').strip()
        inscant = request.POST.get('inscricao', '').strip()
        codelote = request.POST.get('codelote', '').strip()
        uso_imovel = request.POST.get('uso_imovel', '').strip()
        taxacao = request.POST.get('taxacao', '').strip()
        descricao = request.POST.get('descricao', '').strip()
        setorcalcu = request.POST.get('setor_calculo', '').strip()

        # Aplicar filtros dinamicamente
        filtros = {}
        if proprietario:           
            proprietario_normalizado = normalizar_texto(proprietario)
            filtros['proprietar__icontains'] = proprietario_normalizado
        if parcelamento:
            filtros['parcelamen__icontains'] = parcelamento
        if patrimonio:
            filtros['patrimonio__icontains'] = patrimonio
        if inscant:
            filtros['inscant__exact'] = inscant
        if codelote:
            filtros['codelote__exact'] = codelote
        if uso_imovel:
            filtros['usoimovel__icontains'] = uso_imovel
        if taxacao:
            filtros['taxacao__icontains'] = taxacao
        if descricao:
            filtros['descricaot__icontains'] = descricao
        if setorcalcu:
            filtros['setorcalcu__icontains'] = setorcalcu

        # Salvar filtros na sessão
        request.session['filtros'] = filtros
        
        # Buscar os dados com os filtros aplicados
        imoveis = Tiqimo.objects.filter(**filtros).order_by('proprietar')[:20000]  # Limitar a 100 resultados para melhorar desempenho
        contador_filtro = imoveis.count()
        
        # Renderizar o template com os resultados
        context = {
            'imoveis' : imoveis,  
            'contador_filtro':contador_filtro,          
        }
        return render(request, self.template_name, context)
    
class MostrarDados(View):
    template_name = 'home/tabela_dados.html'

    def get(self, request, pk, *args, **kwargs):
        # Obter os dados do objeto pelo ID
        imovel = get_object_or_404(Tiqimo, pk=pk)

        # Dados completos do objeto (ajuste conforme necessário)
        context = {
            'imovel': imovel,  # Passar o objeto único para o template
        }

        return render(request, self.template_name, context)
