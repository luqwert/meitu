# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituItem(scrapy.Item):
    name = scrapy.Field() #姓名
    number = scrapy.Field() #写真套数
    birthday = scrapy.Field() #生日
    constellation = scrapy.Field() #星座
    age = scrapy.Field() #年龄
    height_weight = scrapy.Field() #身高体重
    dimension_cup = scrapy.Field() #三围罩杯
    blood_hometown = scrapy.Field() #血型 #家乡
    career_interest = scrapy.Field() #职业兴趣
    introduction = scrapy.Field() #简介
    tag = scrapy.Field() #标签
    detail_link = scrapy.Field()
    xiezhen_title = scrapy.Field()
    xiezhen_link = scrapy.Field()
    pic_links = scrapy.Field()