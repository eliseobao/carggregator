from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scraper.enums import AutoScout24Enum
from scraper.items import CarItem

# TODO: adapt to CarItem

class AutoScout24Spider(CrawlSpider):
    name = 'autoscout24'
    allowed_domains = ['autoscout24.es']
    start_urls = ['https://www.autoscout24.es/lst?sort=standard&desc=0&ustate=N%2CU&atype=C&cy=E&page='
                  + str(x) + '' for x in range(1, 20)]
    rules = (Rule(LinkExtractor(allow='anuncios'), callback='parse_item', follow=True), )

    @staticmethod
    def parse_item(response):
        item = CarItem()

        item['publisher'] = 'autoscout'
        item['url'] = response.request.url
        item['brand'] = response.css('span.StageTitle_boldClassifiedInfo__L7JmO::text').get().rstrip()
        item['model'] = response.css('span.StageTitle_model__pG_6i.StageTitle_boldClassifiedInfo__L7JmO::text').get()
        item['title'] = item['brand'] + ' ' + item['model']
        item['location'] = response.css('a.scr-link.LocationWithPin_locationItem__pHhCa::text').get()
        item['price_cash'] = response.css('span.StandardPrice_price__X_zzU::text').get()
        item['image'] = response.css('picture.ImageWithBadge_picture__n6hct').css('img').get().split('"')[1]

        categories = response.css('h2.DetailsSectionTitle_text__gsMln::text').getall()
        for idx, elem in enumerate(categories):
            if elem == 'Color y Tapicería':
                index = idx - 1
                break
        item['color'] = response.css('dl.DataGrid_defaultDlStyle__969Qm')[index].css(
            'dd.DataGrid_defaultDdStyle__29SKf.DataGrid_fontBold__r__dO::text').get()

        keys = response.css('div.VehicleOverview_itemTitle__W0qyv::text').getall()
        values = response.css('div.VehicleOverview_itemText__V1yKT::text').getall()

        for key, value in zip(keys, values):
            if key in AutoScout24Enum.list():
                item[AutoScout24Enum(key).name] = value

        yield item

    def parse(self, response, **kwargs):
        pass
