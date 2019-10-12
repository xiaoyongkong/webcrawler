# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PacBrasilItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tipo_obra = scrapy.Field()
    titulo_obra = scrapy.Field()
    orgao_responsavel = scrapy.Field()
    executor = scrapy.Field()
    unidade_federativa = scrapy.Field()
    municipios = scrapy.Field()
    investimento_previsto = scrapy.Field()
    estagio = scrapy.Field()
    dia_data_de_referencia = scrapy.Field()
    mes_data_de_referencia = scrapy.Field()
    ano_data_de_referencia = scrapy.Field()
    pass
