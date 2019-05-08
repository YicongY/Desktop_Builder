# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item


class AresscrapeCPU(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = Field()
    model = Field()
    url = Field()
    name = Field()
    price = Field()
    created_ts = Field()
    rating = Field()
    reviews = Field()
    socket = Field()


class Review(Item):
    cons = Field()
    pros = Field()
    others = Field()
    rating = Field()
    date = Field()


class AresscrapeBoard(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    make = Field()
    model = Field()
    url = Field()
    price = Field()
    name = Field()
    rate = Field()
    reviews = Field()
    socket = Field()


class Aresscrapehdd(Item):
    brand = Field()
    model = Field()
    name = Field()
    url = Field()
    price = Field()
    capacity = Field()
    rating = Field()
    rpm = Field()
    created_ts = Field()
    reviews = Field()


class AresscrapeGPU(Item):
    brand = Field()
    model = Field()
    url = Field()
    name = Field()
    price = Field()
    created_ts = Field()
    rating = Field()
    reviews = Field()
    socket = Field()


class AresscrapeCase(Item):
    brand = Field()
    type = Field()
    compatibility = Field()
    color = Field()
    url = Field()
    price = Field()
    rating = Field()
    created_ts = Field()
    name = Field()
    reviews = Field()


class Aresscraperam(Item):
    brand = Field()
    model = Field()
    name = Field()
    capacity = Field()
    speed = Field()
    ram_type = Field()
    color = Field()
    url = Field()
    price = Field()
    created_ts = Field()
    led = Field()
    rating = Field()
    reviews = Field()


class AresscrapePowersupply(Item):
    brand = Field()
    type = Field()
    power = Field()
    url = Field()
    price = Field()
    rating = Field()
    created_ts = Field()
    name = Field()
    reviews = Field()