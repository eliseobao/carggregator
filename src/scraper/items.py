# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field


class MotorEsItem(Item):
    url = Field()
    title = Field()
    location = Field()
    brand = Field()
    model = Field()
    version = Field()
    price_cash = Field()
    price_financed = Field()
    fuel = Field()
    hp = Field()
    odometer = Field()
    bodywork = Field()
    registration_date = Field()
    transmission = Field()
    gears = Field()
    seats = Field()
    doors = Field()
    color = Field()


class AutoScout24Item(Item):
    url = Field()
    location = Field()
    brand = Field()
    model = Field()
    version = Field()
    extras = Field()
    price_cash = Field()
    odometer = Field()
    transmission = Field()
    registration_date = Field()
    fuel = Field()
    hp = Field()
    seller = Field()

