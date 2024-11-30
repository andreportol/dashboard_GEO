import django_filters
from .models import Imoveis


class ImoveisFilter(django_filters.FilterSet):
    codlote = django_filters.CharFilter(field_name='codlote', lookup_expr='icontains', label='Codlote')
    inscant = django_filters.CharFilter(field_name='inscant', lookup_expr='icontains', label='Inscant')
    parcelament = django_filters.CharFilter(field_name='parcelament', lookup_expr='icontains', label='Parcelament')
    proprietar = django_filters.CharFilter(field_name='proprietar', lookup_expr='icontains', label='Proprietar')
    patrimonio = django_filters.CharFilter(field_name='patrimonio', lookup_expr='icontains', label='Patrimonio')
    taxacao = django_filters.CharFilter(field_name='taxacao', lookup_expr='icontains', label='Taxação')
    descricao = django_filters.CharFilter(field_name='descricao', lookup_expr='icontains', label='Descrição')
    usoimovel = django_filters.CharFilter(field_name='usoimovel', lookup_expr='icontains', label='Uso do Imóvel')
    setorcalcu = django_filters.CharFilter(field_name='setorcalcu', lookup_expr='icontains', label='Setor Cálculo')

    class Meta:
        model = Imoveis
        fields = [
            'codlote',
            'inscant',
            'parcelament',
            'proprietar',
            'patrimonio',
            'taxacao',
            'descricao',
            'usoimovel',
            'setorcalcu',
        ]

