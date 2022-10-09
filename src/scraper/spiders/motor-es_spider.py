from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scraper.enums import MotorEsEnum
from scraper.items import MotorEsItem


class MotorEsSpider(CrawlSpider):
    name = "motor.es"
    allowed_domains = ["motor.es"]
    start_urls = ["https://www.motor.es/coches-segunda-mano"]
    rules = (Rule(LinkExtractor(allow='coches-segunda-mano'), callback='parse_item', follow=True),)

    def parse_item(self, response):

        item = MotorEsItem()
        title = response.css('.principal h1 ::text').get()

        if title is not None:
            item["title"] = title
            item["url"] = response.request.url
            item["location"] = response.request.url.split('/')[4].replace('-', ' ').title()

            keys = response.css('.ficha.zona-contenido dt ::text').getall()
            values = response.css('.ficha.zona-contenido dd ::text').getall()
            if 'Distintivo ambiental' in keys: keys.remove('Distintivo ambiental')

            for key, value in zip(keys, values):
                if key in MotorEsEnum.list():
                    item[MotorEsEnum(key).name] = value

            yield item
