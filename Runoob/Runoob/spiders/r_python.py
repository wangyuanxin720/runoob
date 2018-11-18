# -*- coding: utf-8 -*-
import scrapy
from urllib import request
from Runoob.Handle_text import deal_html
from Runoob.items import RunoobItem
from Runoob.settings import IMAGES_STORE
class RPythonSpider(scrapy.Spider):
    name = 'r_python'
    allowed_domains = ['runoob.com']
    start_urls = ['http://www.runoob.com/python3/python3-tutorial.html']

    def parse(self, response):
        title_list = response.xpath('//div[@id="leftcolumn"]//a')
        for a in title_list:
            title = a.xpath('.//text()').extract_first().strip()
            url = request.urljoin(response.url, a.xpath('.//@href').extract_first().strip())
            yield scrapy.Request(url, callback=self.parse_info, meta={'title': title})

    def parse_info(self, response):
        title = response.meta["title"]
        html = response.xpath('//div[@id="content"]').extract_first()
        html, img_list = deal_html(html)
        item = RunoobItem()
        item['html'] = html
        item['title'] = title
        item['column'] = 'Python3'
        item['site'] = '菜鸟教程'

        item['attachments'] = [{
            'Not_stitching' : img_url,
            "original_file_name": request.urljoin(response.url, img_url),
            'IMAGES_STORE': IMAGES_STORE,
            "generatce_file_name": '',
        } for img_url in img_list if img_list]
        yield item
