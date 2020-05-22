# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FangspiderLoupanItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    huxin = scrapy.Field()
    area = scrapy.Field()
    address = scrapy.Field()
    tag = scrapy.Field()
    phone_plat = scrapy.Field()
    unit_price = scrapy.Field()
    city = scrapy.Field()

class NewhouseIndexItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    unit_price = scrapy.Field()
    tag = scrapy.Field()
    louaddress = scrapy.Field()
    sale_time = scrapy.Field()
    delivery_time = scrapy.Field()
    huxin_main = scrapy.Field()
    other_name = scrapy.Field()
    part = scrapy.Field()
    compart = scrapy.Field()
    city = scrapy.Field()

class NewhouseDetailItem(scrapy.Item):
    url = scrapy.Field()
   #wuye = scrapy.Field()
    buiding_type = scrapy.Field()
    alright = scrapy.Field()
    #alright_note = scrapy.Field()
    location = scrapy.Field()
    property_ = scrapy.Field()
    status = scrapy.Field()
    marker_address = scrapy.Field()
    phone_plat = scrapy.Field()
    #presale = scrapy.Field()
    floor_area = scrapy.Field()
    gross_area = scrapy.Field()
    gross_area_ratio = scrapy.Field()
    greening_ratio = scrapy.Field()
    parking = scrapy.Field()
    counter_buidings = scrapy.Field()
    counter_households = scrapy.Field()
    wuye_corp = scrapy.Field()
    wuye_cost = scrapy.Field()
    wuye_note = scrapy.Field()
    status_buidings = scrapy.Field()
    #nearby_loupan = scrapy.Field()
    #with_loupan = scrapy.Field()
    #note = scrapy.Field()
    sale_time = scrapy.Field()
    poi = scrapy.Field()
    profile = scrapy.Field()
    presale = scrapy.Field()
    price_history = scrapy.Field()

class NewhouseKaipanDetail(scrapy.Item):
    kaipan = scrapy.Field()
    url = scrapy.Field()

class NewhouseKaipanPostDetail(scrapy.Item):
    url = scrapy.Field()
    post_list = scrapy.Field()

class NewhouseDeliveryTimeDetailIndex(scrapy.Item):
    url = scrapy.Field()
    delivery_time = scrapy.Field()
    