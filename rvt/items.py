# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RVItem(scrapy.Item):

    product_uid = scrapy.Field()
    year = scrapy.Field()
    model = scrapy.Field()
    length = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    main_photo = scrapy.Field()
    photos = scrapy.Field()
    contact_person = scrapy.Field()
    address = scrapy.Field()
    phone1 = scrapy.Field()
    email = scrapy.Field()
    created = scrapy.Field()
