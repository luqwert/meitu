# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
import re

class MeituPipeline(object):
    def __init__(self):
        self.mritu1_count = 0
        # self.youma_count = 0
        # self.oumei_count = 0
    def process_item(self, item, spider):
        # name = item['name']
        dirname1 = 'J:\\写真\\%s\\' % item['name']
        if not os.path.exists(dirname1):
            os.makedirs(dirname1)
        dirname2 = dirname1 + item['xiezhen_title'] + '\\'
        if not os.path.exists(dirname2):
            os.makedirs(dirname2)
        filename = re.search(r'(?<=/)\d+(?=.jpg)', item['pic_links']).group() + '.jpg'
        print(filename)
        if os.path.exists(dirname2 + filename):
            pass
        else:
            with open(dirname2 + filename, 'wb') as f:

                print(dirname2 + filename, item['pic_links'])
                req = requests.get(item['pic_links']).content
                f.write(req)
        # print(item)
        self.mritu1_count += 1
        print('已下载 %s, %d:' % (spider.name, self.mritu1_count))

