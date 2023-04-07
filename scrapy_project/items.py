# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AirplanesItem(scrapy.Item):
    image_urls = scrapy.Field()
    text = scrapy.Field()
