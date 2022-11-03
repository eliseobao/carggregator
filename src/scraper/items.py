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
    gears = Field()
    seats = Field()
    doors = Field()
    color = Field()

class AutocasionItem(Item):
    url = Field()
    source = Field()
    title = Field()
    price_cash = Field()
    price_financed = Field()
    registration_date = Field()
    odometer = Field()
    transmission = Field()
    fuel = Field()
    hp = Field()
    warranty = Field()
    bodywork = Field()
    color = Field()
    environmental_badge = Field()
