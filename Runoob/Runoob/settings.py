# -*- coding: utf-8 -*-

# Scrapy settings for Runoob project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Runoob'

SPIDER_MODULES = ['Runoob.spiders']
NEWSPIDER_MODULE = 'Runoob.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


ITEM_PIPELINES = {
    'Runoob.pipelines.SaveImgPipeline': 301,
    'Runoob.pipelines.RunoobPipeline': 304,
}

MONGO_URI = '127.0.0.1:27017'
MONGO_DATABASE = 'shuama'
MONGO_COLLECTION = 'runoob'




IMAGES_STORE = '/data/shuama/runoob/'