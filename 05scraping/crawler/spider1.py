import scrapy

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:5000/']

    def parse(self, response):
        for radek in response.css("#seznam > tbody > tr"):
            name = radek.css("td:nth-child(1) > a::text").extract_first()
            phone = radek.css("td:nth-child(2) ::text").extract_first()
            email = radek.css("td:nth-child(3) > a::text").extract_first()

            yield {
                'name': name,
                'phone': phone,
                'email': email,
                }

# otevreni jsnu
#import json
#data = json.load(open('data.json'))

#v bash == scrapy runspider spider1.py -o data.json
