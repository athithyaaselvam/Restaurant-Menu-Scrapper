# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NabsItem(scrapy.Item):
    # define the fields for your item here like:
    state = scrapy.Field()
    studentPresident = scrapy.field()
    affiliatePresident = scrapy.field()

