from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapper.items import MotorEsItem

class MotorEsSpider(CrawlSpider):
    name = "motor.es"
    allowed_domains = ["motor.es"]
    start_urls = ["https://www.motor.es/coches-segunda-mano"]
    rules = (Rule(LinkExtractor(allow='coches-segunda-mano'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        item = MotorEsItem()

        item["price"] = response.css('.precio ::text').get().strip()
        # TODO more items

        if item["price"] is not None:
            yield item

