# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tiqimo(models.Model):
    codelote = models.CharField(max_length=11, blank=True, null=True)
    codimo = models.CharField(max_length=3, blank=True, null=True)
    digito = models.CharField(max_length=1, blank=True, null=True)
    inscant = models.CharField(max_length=11, blank=True, null=True)
    faceloc = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    tipoloc = models.CharField(max_length=120, blank=True, null=True)
    ruaimo = models.CharField(max_length=120, blank=True, null=True)
    nrporta = models.CharField(max_length=6, blank=True, null=True)
    complement = models.CharField(max_length=100, blank=True, null=True)
    parcelamen = models.CharField(max_length=100, blank=True, null=True)
    quadra = models.CharField(max_length=5, blank=True, null=True)
    lote = models.CharField(max_length=5, blank=True, null=True)
    proprietar = models.CharField(max_length=120, blank=True, null=True)
    compromiss = models.CharField(max_length=120, blank=True, null=True)
    administra = models.CharField(max_length=120, blank=True, null=True)
    TIPO_CHOICES_PATRIMONIO = (
        ('PARTICULAR', 'PARTICULAR'),
        ('ENTIDADES', 'ENTIDADES'),
        ('PUBLICO', 'PUBLICO'),
        ('RELIGIOSO', 'RELIGIOSO'),
    )
    patrimonio = models.CharField(verbose_name= 'Patrimônio', max_length=36, blank=True, null=True, choices=TIPO_CHOICES_PATRIMONIO,)
    TIPO_CHOICES_TAXACAO = (
        ('ATIVADA', 'ATIVADA'),
        ('INIB CONTA', 'INIB CONTA'),
        ('IMUNE', 'IMUNE'),
        ('ISENTO', 'ISENTO'),
    )
    taxacao = models.CharField(verbose_name='Taxação', max_length=36, blank=True, null=True,choices=TIPO_CHOICES_TAXACAO,)
    TIPO_CHOICES_DESCRICAOT = (
        ('null', 'null'),
        ('NORMAL', 'NORMAL'),
        ('RURAL', 'RURAL'),
        ('AUTARQUIA', 'AUTARQUIA'),
        ('RELIGIOSO', 'RELIGIOSO'),
        ('RELIGIOSO-FE', 'RELIGIOSO-FE'),
        ('IGREJA', 'IGREJA'),
        ('PUB ESTADUAL', 'PUB ESTADUAL'),
        ('PUB FEDERAL', 'PUB FEDERAL'),
        ('PUB MUNICIPAL', 'PUB MUNICIPAL'),
        ('SIST ANTERIOR', 'SIST ANTERIOR'),
        ('FEDERACAO', 'FEDERACAO'),
        ('SINDICATO TRAB', 'SINDICATO TRAB'),
        ('APOSENTADO', 'APOSENTADO'),
        ('APOSENTADO/PENS', 'APOSENTADO/PENS'),
        ('ASSIST SOC-FE', 'ASSIST SOC-FE'),
        ('ASSIST SOCIAL', 'ASSIST SOCIAL'),
        ('ASSOCIACAO', 'ASSOCIACAO'),
        ('ASSOCIACAO-FE', 'ASSOCIACAO-FE'),
        ('CLUBE SOCIAL', 'CLUBE SOCIAL'),
        ('CONSELHO', 'CONSELHO'),
        ('CONSELHO-FE', 'CONSELHO-FE'),
        ('CRECHE', 'CRECHE'),
        ('ENTIDADE SOCIAL', 'ENTIDADE SOCIAL'),
        ('ESCOLA', 'ESCOLA'),
        ('EXPEDICIONARIO', 'EXPEDICIONARIO'),
        ('FUNDACAO', 'FUNDACAO'),
        ('HIST/CULT/ECOL', 'HIST/CULT/ECOL'),
        ('INSTIT CEPC', 'INSTIT CEPC'),
        ('ITR', 'ITR'),
        ('MACONARIA', 'MACONARIA'),
        ('PARTIDO POLIT', 'PARTIDO POLIT'),
    )    
    descricaot = models.CharField(max_length=100, blank=True, null=True, choices=TIPO_CHOICES_DESCRICAOT)
    TIPO_CHOICES_USO_IMOVEL = (
        ('RESIDENCIAL', 'RESIDENCIAL'),
        ('TERRITORIAL', 'TERRITORIAL'),
        ('FINALID ESSENCIAIS', 'FINALID ESSENCIAIS'),
        ('COMERCIAL', 'COMERCIAL'),
        ('SERVICOS', 'SERVICOS'),
        ('INDUSTRIAL', 'INDUSTRIAL'),
        ('MISTO', 'MISTO'),
        ('RELIGIOSO', 'RELIGIOSO'),
        ('MCMV (SUSPENSO SUB JUDICE)', 'MCMV (SUSPENSO SUB JUDICE)'),
        ('PUBLICO', 'PUBLICO'),
        ('RURAL AGROPECUARIO PRED', 'RURAL AGROPECUARIO PRED'),
        ('RURAL TERRITORIAL', 'RURAL TERRITORIAL'),
        ('RURAL SERV/COMERCIO', 'RURAL SERV/COMERCIO'),
        ('RURAL SITIO RECREIO TERR', 'RURAL SITIO RECREIO TERR'),
        ('RURAL INDUSTRIAL', 'RURAL INDUSTRIAL'),
        ('RURAL AGROPECUARIO TERR', 'RURAL AGROPECUARIO TERR'),
        ('RURAL SITIO RECREIO PRED', 'RURAL SITIO RECREIO PRED'),
        ('RURAL FIN. ESSENCIAIS', 'RURAL FIN. ESSENCIAIS'),
        ('MINHA CASA MINHA VIDA', 'MINHA CASA MINHA VIDA'),
    )
    usoimovel = models.CharField(max_length=36, blank=True, null=True, choices=TIPO_CHOICES_USO_IMOVEL)
    codaverbac = models.CharField(max_length=15, blank=True, null=True)
    agua = models.CharField(max_length=1, blank=True, null=True)
    coletalixo = models.CharField(max_length=1, blank=True, null=True)
    coletivo = models.CharField(max_length=1, blank=True, null=True)
    esgoto = models.CharField(max_length=1, blank=True, null=True)
    ilumpublic = models.CharField(max_length=1, blank=True, null=True)
    limpeza = models.CharField(max_length=1, blank=True, null=True)
    meiofio = models.CharField(max_length=1, blank=True, null=True)
    pavimentac = models.CharField(max_length=1, blank=True, null=True)
    redeeletri = models.CharField(max_length=1, blank=True, null=True)
    redetelefo = models.CharField(max_length=1, blank=True, null=True)
    setorcalcu = models.IntegerField(blank=True, null=True)
    codregiao = models.IntegerField(blank=True, null=True)
    codbairro = models.CharField(max_length=4, blank=True, null=True)
    testada = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    nrtestada = models.IntegerField(blank=True, null=True)
    areaterren = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    arealote = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    areapiscin = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    quadraespo = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    tipolote = models.CharField(max_length=36, blank=True, null=True)
    formatoter = models.CharField(max_length=36, blank=True, null=True)
    caractlimi = models.CharField(max_length=36, blank=True, null=True)
    topografia = models.CharField(max_length=36, blank=True, null=True)
    pedologia = models.CharField(max_length=36, blank=True, null=True)
    frente = models.CharField(max_length=36, blank=True, null=True)
    calcada = models.CharField(max_length=2, blank=True, null=True)
    areaedificimovel = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valorvenal = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valorconst = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    avaliacao = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fracaoidea = models.DecimalField(max_digits=6, decimal_places=5, blank=True, null=True)
    dataaltera = models.DateField(blank=True, null=True)
    fracaocon = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    ruacorresp = models.CharField(max_length=120, blank=True, null=True)
    nrportacor = models.CharField(max_length=6, blank=True, null=True)
    complcorre = models.CharField(max_length=100, blank=True, null=True)
    bairrocorr = models.CharField(max_length=50, blank=True, null=True)
    cidadecorr = models.CharField(max_length=40, blank=True, null=True)
    estadocorr = models.CharField(max_length=2, blank=True, null=True)
    cepcorresp = models.CharField(max_length=9, blank=True, null=True)
    dataavaliacao = models.DateField(blank=True, null=True)
    facequadra = models.CharField(max_length=8, blank=True, null=True)
    areaedificlote = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    valorterrenolote = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valoredificlote = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    valortotallote = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    averbacao = models.IntegerField(blank=True, null=True)
    processoaverb = models.CharField(max_length=15, blank=True, null=True)
    datprocaverb = models.DateField(blank=True, null=True)
    nraverbacao = models.IntegerField(blank=True, null=True)
    livroaverb = models.CharField(max_length=6, blank=True, null=True)
    folhaaverb = models.CharField(max_length=4, blank=True, null=True)
    cartorioaverb = models.CharField(max_length=15, blank=True, null=True)
    dataverb = models.DateField(blank=True, null=True)
    datregaverb = models.DateField(blank=True, null=True)
    matriculaaverb = models.CharField(max_length=120, blank=True, null=True)
    codlogradouro = models.CharField(max_length=6, blank=True, null=True)
    codparcelamento = models.CharField(max_length=6, blank=True, null=True)
    nomeregiao = models.CharField(max_length=120, blank=True, null=True)
    nomebairro = models.CharField(max_length=100, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=18, blank=True, null=True)
    codlot = models.CharField(max_length=3, blank=True, null=True)
    # Campo desnormalizado -> campo criado fora do banco de dados existente
    valor_iptu_estimado = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True
    )  

    class Meta:
        managed = False
        db_table = 'tiqimo'
        verbose_name = 'Inscrição Imobiliária'
        verbose_name_plural = 'Inscrições'

    # método chamada toda vez que um (1) objeto for inserido ou atualizado no banco de dados.
    def save(self, *args, **kwargs):
        if self.avaliacao and self.aliquota and self.taxacao == 'ATIVADA':
            self.valor_iptu_estimado = self.avaliacao * (self.aliquota / 100)
        else:
            self.valor_iptu_estimado = 0
        super().save(*args,**kwargs)

    def __str__(self):
        return self.inscant