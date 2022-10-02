import scrapy


class QuotesSpider(scrapy.Spider):
    name = "motor.es"
    start_urls = [
        'https://www.motor.es/coches-segunda-mano/',
    ]

    def parse(self, response):

        for car_link in response.css('h3 .coche-link ::attr(href)').getall():
            print(f'Link: {car_link}')

        next_page = response.css('.js-next-page ::attr(href)').get()
        print(f'Next page: {next_page}')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)