import scrapy

class FlexicarSpider(scrapy.Spider):

    #name of the spider
    name = 'flexicar'

    #domain that we will scrap
    allowed_domains = ['flexicar.es']

    #url of the page that we will start scraping
    start_urls = ['https://www.flexicar.es/coches-segunda-mano/']

    '''
    def start_requests(self):
        yield scrapy.Request('https://www.flexicar.es/coches-segunda-mano/', meta={'playwright': True})'''

    def parse(self, response):

        #looping through the cars
        cars = response.css('.MuiGrid-grid-sm-6.MuiGrid-grid-lg-4')
        for car in cars:
            yield {
                'name': car.css('h2.MuiTypography-root.MuiTypography-h6::text').get(),
                'url': car.css('a.MuiTypography-root.MuiLink-root.MuiLink-underlineNone.jss44').attrib['href'],
            }


    '''def parse(self, response):
        yield {
            'text': response.text,
        }'''
