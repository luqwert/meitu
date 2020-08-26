# -*- coding: utf-8 -*-
import scrapy
from meitu.items import MeituItem
import re
from meitu import settings

class Mritu1Spider(scrapy.Spider):
    name = 'mritu1'
    allowed_domains = ['meituri.com','hywly.com','tujigu.com']
    start_urls = ['https://www.meituri.com/zhongguo/']

    def parse(self, response):
        li_list = response.xpath("/html/body/div[2]/ul/li")
        for li in li_list:
            detail_link = li.xpath("./p/a/@href").extract_first()
            yield scrapy.Request(
                detail_link,
                callback=self.parse_detail1,
            )
        #找到下一页的url地址
        # next_url = response.xpath('//a[contains(text(), "下一页")]/@href').extract_first()
        # # print(next_url)
        # a = response.xpath('//*[@id="pages"]/span/text()').extract_first()
        # b = re.search(r'(?<=/)\d+(?=.html)', next_url).group()
        # # print(a, b)
        # if a != b:
        #     next_url = 'https://www.meituri.com' + next_url
        #     # print(next_url)
        #     yield scrapy.Request(next_url,
        #                          callback=self.parse,
        #                          dont_filter=True,
        #                          )

    def parse_detail1(self, response):
        number = len(response.xpath('/html/body/div[7]/ul//li'))
        if response.xpath('//*[@id="pages"]/a[contains(text(), "下一页")]/text()').extract_first() is None:
            for i in range(number):
                item = MeituItem()
                item["name"] = response.xpath("/html/body/div[2]/div[2]/h1/text()").extract_first()
                item["birthday"] = response.xpath('/html/body/div[2]/div[2]/p[1]/text()[1]').extract_first()
                item["constellation"] = response.xpath('/html/body/div[2]/div[2]/p[1]/text()[2]').extract_first()
                item["age"] = response.xpath('/html/body/div[2]/div[2]/p[1]/text()[3]').extract_first()
                item["height_weight"] = response.xpath('/html/body/div[2]/div[2]/p[2]/text()').extract()
                item["dimension_cup"] = response.xpath('/html/body/div[2]/div[2]/p[3]/text()').extract()
                item["blood_hometown"] = response.xpath('/html/body/div[2]/div[2]/p[4]/text()').extract()
                item["career_interest"] = response.xpath('/html/body/div[2]/div[2]/p[5]/text()').extract()
                item["introduction"] = response.xpath('/html/body/div[2]/div[5]/text()').extract()
                item["tag"] = response.xpath('/html/body/div[2]/div[5]/p//a/text()').extract()
                item["number"] = response.xpath('/html/body/div[4]/span/text()').extract_first()
                item["xiezhen_title"] = response.xpath('/html/body/div[7]/ul/li[%d]/p[3]/a/text()' % (i+1) ).extract_first()
                item["xiezhen_link"] = response.xpath('/html/body/div[7]/ul/li[%d]/p[3]/a/@href' % (i+1) ).extract_first()
                yield scrapy.Request(item["xiezhen_link"],
                                     callback=self.parse_pic,
                                     meta={'b': item}
                                     )
            # print('小于40写真详情')
        else:
            for i in range(40):
                item = MeituItem()
                item["name"] = response.xpath("/html/body/div[2]/div[2]/h1/text()").extract_first()
                item["birthday"] = response.xpath('/html/body/div[2]/div[2]/p[1]/text()[1]').extract_first()
                item["constellation"] = response.xpath('/html/body/div[2]/div[2]/p[1]/text()[2]').extract_first()
                item["age"] = response.xpath('/html/body/div[2]/div[2]/p[1]/text()[3]').extract_first()
                item["height_weight"] = response.xpath('/html/body/div[2]/div[2]/p[2]/text()').extract()
                item["dimension_cup"] = response.xpath('/html/body/div[2]/div[2]/p[3]/text()').extract()
                item["blood_hometown"] = response.xpath('/html/body/div[2]/div[2]/p[4]/text()').extract()
                item["career_interest"] = response.xpath('/html/body/div[2]/div[2]/p[5]/text()').extract()
                item["introduction"] = response.xpath('/html/body/div[2]/div[5]/text()').extract()
                item["tag"] = response.xpath('/html/body/div[2]/div[5]/p//a/text()').extract()
                item["number"] = response.xpath('/html/body/div[4]/span/text()').extract_first()
                item["xiezhen_title"] = response.xpath('/html/body/div[7]/ul/li[%d]/p[3]/a/text()' % (i+1)).extract_first()
                item["xiezhen_link"] = response.xpath('/html/body/div[7]/ul/li[%d]/p[3]/a/@href' % (i+1)).extract_first()
                yield scrapy.Request(item["xiezhen_link"],
                                     callback=self.parse_pic,
                                     meta={'b': item},
                                     )
            # print('大于40写真详情')
            #下一页
            # next_url = 'https://www.meituri.com' + response.xpath('//*[@id="pages"]/a[contains(text(), "下一页")]/@href').extract_first()
            # # print(next_url)
            # yield scrapy.Request(next_url,
            #                      callback=self.parse_detail1,
            #                      dont_filter=True,
            #                      )
        # print(item)


    def parse_pic(self, response):

        item = response.meta['b']
        number = len(response.xpath('/html/body/div[4]//img'))
        # print(number)
        next_url2 = response.xpath('//a[contains(text(), "下一页")]/@href').extract_first()
        # print('图片下一页：' + next_url2)
        a = int(response.xpath('//*[@id="pages"]/span/text()').extract_first())
        b = int(re.search(r'(?<=/)\d+(?=.html)', next_url2).group())
        # print('a b ', a != b)
        if a != b:
            for i in range(5):
                # item = MeituItem()
                item['pic_links'] = response.xpath('/html/body/div[4]/img[%d]/@src' % (i+1)).extract_first()
                yield item
                # print(item[])
            # print('大于5图片链接已添加')
            yield scrapy.http.Request(next_url2,
                                      callback=self.parse_pic,
                                      dont_filter=True,
                                      meta={'b': item}
                                      )
        else:
            for i in range(number):
                # item = MeituItem()
                item['pic_links'] = response.xpath('/html/body/div[4]/img[%d]/@src' % (i+1)).extract_first()
                yield item
                # print(item)
            # print('小于5图片链接已添加')
        # yield item


