# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class CarItem(Item):
    url = Field()
    title = Field()
    publisher = Field()
    image = Field()
    location = Field()
    brand = Field()
    model = Field()
    price_cash = Field()
    price_financed = Field()
    fuel = Field()
    hp = Field()
    odometer = Field()
    registration_date = Field()
    transmission = Field()
