# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors  import LinkExtractor
from PAC_BRASIL.items import PacBrasilItem

class PacSpider(CrawlSpider):
    name = 'pac'
    allowed_domains = ['www.pac.gov.br']
    start_urls = ['http://www.pac.gov.br/infraestrutura-logistica/rodovias',
        'http://www.pac.gov.br/infraestrutura-logistica/ferrovias',
        'http://www.pac.gov.br/infraestrutura-logistica/portos',
        'http://www.pac.gov.br/infraestrutura-logistica/hidrovias',
        'http://www.pac.gov.br/infraestrutura-logistica/aeroportos',
        'http://www.pac.gov.br/infraestrutura-logistica/defesa',
        'http://www.pac.gov.br/infraestrutura-logistica/comunicacoes',
        'http://www.pac.gov.br/infraestrutura-logistica/ciencia-e-tecnologia']
    rules = (
            Rule(LinkExtractor(allow=(), restrict_css=('.pag_prox > a',)),
                callback="parse_item",
             follow=True),)
    #def parse(self,response):
        #print('Processing..' + response.url)
        #pass
    def parse_detail_page(self,response):
        table = response.css('#dados_obra > tbody')
        rows = table.xpath('//tr')
        rows_texts = rows.xpath('td//text()')
        item = PacBrasilItem()
        item['tipo_obra'] = response.css('#breadcrumb > .construct > p > a::text')[2].extract()
        item['titulo_obra'] = response.css('.titulo_pagina::text').extract()[0]
        item['orgao_responsavel'] = rows_texts[0].extract()
        item['executor'] = rows_texts[1].extract()
        item['unidade_federativa'] = rows_texts[2].extract()
        if (len(rows_texts) > 10):
            item['municipios']  = rows_texts[3].extract()
            item['investimento_previsto'] = rows_texts[4].extract()
            item['estagio'] = rows.xpath('td//text()')[5].extract()
            item['ano_data_de_referencia'] = rows.xpath('td//text()')[10].extract()
            item['mes_data_de_referencia'] = rows.xpath('td//text()')[8].extract()
            item['dia_data_de_referencia'] = rows.xpath('td//text()')[6].extract()
        else:
            item['municipios']  = 'NULL'
            item['investimento_previsto'] = rows_texts[3].extract()
            item['estagio'] = rows.xpath('td//text()')[4].extract()
            item['ano_data_de_referencia'] = rows.xpath('td//text()')[9].extract()
            item['mes_data_de_referencia'] = rows.xpath('td//text()')[7].extract()
            item['dia_data_de_referencia'] = rows.xpath('td//text()')[5].extract()
        yield item
        
    def parse_item(self, response):
        print('Processing..' + response.url)
        item_links = response.css('#lista_obras_do_tipo > li > a::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)