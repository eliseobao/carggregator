import scrapy


class QuotesSpider(scrapy.Spider):
    name = "coches.net"
    start_urls = [
        'https://www.coches.net/segunda-mano/?pg=1',
    ]

    def parse(self, response):
        for card in response.css('.sui-AtomCard-info'):
            yield {
                'name': card.css('.mt-CardBasic-title').get(),
            }

        next_page = response.css('.sui-MoleculePagination-item:nth-child(8) .sui-AtomButton--circular a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)