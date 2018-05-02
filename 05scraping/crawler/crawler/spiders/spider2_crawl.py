# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Spider2Spider(CrawlSpider):
    name = 'spider2'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:5000/']

    rules = (
        Rule(LinkExtractor(allow=r'user/.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        name = response.css("dd:nth-child(2)::text").extract_first()
        yield {
            'name': name,
            }
