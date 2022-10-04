# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FlexicarItem(Item):
    # define the fields for your item here like:
    year = Field()
    kilometers = Field()
    fuel = Field()
    doors_seats = Field()
    engine = Field()
    color = Field()
    gear_shift = Field()
    consumption = Field()
    tax_deductible = Field()
