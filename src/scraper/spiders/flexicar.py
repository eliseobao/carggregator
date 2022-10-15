from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.enums import FlexicarEnum
from scraper.items import FlexicarItem


class FlexicarSpider(CrawlSpider):

    name = "flexicar"
    allowed_domains = ["flexicar.es"]
    start_urls = ['https://www.flexicar.es/coches-segunda-mano/']
    rules = (Rule(LinkExtractor(allow='coches-ocasion'), callback='parse_item', follow=True),)

    @staticmethod
    def parse_item(response):
        item = FlexicarItem()
        item['url'] = response.request.url
        car = response.css('h2.MuiTypography-root.MuiTypography-h6::text').getall()
        item['brand'], item['model'] = car[0], car[2]
        item['version'] = response.css('h2.MuiTypography-subtitle1::text').get()

        keys = response.css('p.MuiTypography-root.jss67.MuiTypography-body2::text').getall()

        #TO-DO: these lines split 'Puertas / Asientos' into two different elements
        #keys = [element.split('/') for element in keys]
        #keys = [element.strip() for element in [element for sublist in keys for element in sublist]]

        values = response.css('strong.jss68::text').getall()

        for key, value in zip(keys, values):
            if key in FlexicarEnum.list():
                item[FlexicarEnum(key).name] = value

        yield item

    def parse(self, response, **kwargs):
        pass
