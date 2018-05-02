#vyparsovat majitele a cislo k uctu, pak popripade i z ostatnich stran
#udelat seznam uctu
# https://www.fio.cz/bankovni-sluzby/bankovni-ucty/transparentni-ucet/vypis-transparentnich-uctu

import scrapy

class Fio1Spider(scrapy.Spider):
    name = 'Fio'
    allowed_domains = ['fio']
    start_urls = ['https://www.fio.cz/bankovni-sluzby/bankovni-ucty/transparentni-ucet/vypis-transparentnich-uctu']

    def parse(self, response):
        account_name =
        account_number =
