import scrapy
from scrapy.spiders import SitemapSpider

class Spider3Spider(SitemapSpider):
  name = 'spider3'
  allowed_domains = ["localhost"]

  sitemap_urls = [...]
  sitemap_rules = [...]
