# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class NegcopyrightspiderItem(scrapy.Item):
    title = Field()
    text = Field()
    url = Field()

class DBItems(scrapy.Item):
    copyright_string = Field()
    source = Field()
    datetime = Field()