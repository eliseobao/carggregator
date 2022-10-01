import scrapy

class FlexicarSpider(scrapy.Spider):

    #name of the spider
    name = 'flexicar'

    def start_requests(self):
        yield scrapy.Request('https://www.flexicar.es/coches-segunda-mano/', meta={'playwright': True})


    def parse(self, response):
        yield {
            'text': response.text,
        }
