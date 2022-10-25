import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.enums import AutocasionEnum
from scraper.items import AutocasionItem


class AutocasionSpider(CrawlSpider):

    name = "autocasion"
    allowed_domains = ['autocasion.com']
    start_urls = ['https://www.autocasion.com/coches-ocasion']

    custom_settings = {'CLOSESPIDER_PAGECOUNT': 20}

    rules = (
        Rule(LinkExtractor(allow='coches-segunda-mano'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        card = response.css('div.bloque.titulo-ficha')
        name_p1 = card.css('h1::text').get()
        price_cash = response.css('div.precio').css('span::text').get()
        price_financed = response.css('div.precio.financiado').css('span::text').get()

        if name_p1 is not None:

            name_p2 = response.css('div.bloque.titulo-ficha').css('h1').css('span::text').get()
            car_features = response.css('ul.datos-basicos-ficha')
            keys = self.process_list(car_features.css('li::text').getall())
            values = self.process_list(car_features.css('li').css('span::text').getall())

            item = AutocasionItem()
            item['title'] = name_p1.strip() + " " + name_p2.strip() if name_p2 is not None else name_p1.strip()
            item['url'] = response.request.url
            item['source'] = 'Autocasion'
            item['price_cash'] = price_cash
            if price_financed is not None:
                item['price_financed'] = price_financed

            for key, value in zip(keys, values):
                if key in AutocasionEnum.list():
                    item[AutocasionEnum(key).name] = value

            yield item

    def process_list(self, l_in):
        l_out = []

        for i in range(len(l_in)):
            text = l_in[i].strip()
            if text != '':
                l_out.append(text)

        return l_out
