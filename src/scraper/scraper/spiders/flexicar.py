from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.items import FlexicarItem

class FlexicarSpider(CrawlSpider):
    name = "flexicar"
    allowed_domains = ["flexicar.es"]
    start_urls = ["https://www.flexicar.es/coches-segunda-mano/"]
    rules = (Rule(LinkExtractor(allow='coches-ocasion'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        item = FlexicarItem()
        car_features = response.css('strong.jss68::text')

        if (len(car_features) == 9):
            item['year'] = car_features[0].get()
            item['kilometers'] = car_features[1].get()
            item['fuel'] = car_features[2].get()
            item['doors_seats'] = car_features[3].get()
            item['engine'] = car_features[4].get()
            item['color'] = car_features[5].get()
            item['gear_shift'] = car_features[6].get()
            item['consumption'] = car_features[7].get()
            item['tax_deductible'] = car_features[8].get()

        if item['year'] is not None:
            yield item