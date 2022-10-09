import scrapy


class AutocasionSpider(scrapy.Spider):
    name = "autocasion"

    start_urls = [
        'https://www.autocasion.com/coches-ocasion'
    ]

    def parse(self, response):

        # check if there is an error
        if response.css('div.alert.alert-warning').get() is None:
            for car_ad in response.css('article.anuncio'):
                content = car_ad.css('div.contenido-anuncio')
                yield {
                    'url': car_ad.css('a::attr(href)').get(),
                    'name': content.css('h2::text').get(),
                    'price': content.css('p.precio')[0].css('span::text').get(),
                    'features': content.css('ul').css('li::text').getall()
                }

            navegation = response.css('div.paginacion').css('ul').css('li')
            # [-1] --> last item, bc the first can be the previus page
            next_page = response.urljoin(navegation.css('a::attr(href)').getall()[-1])
            yield scrapy.Request(next_page, callback=self.parse)


