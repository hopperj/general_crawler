# @Author: Jason Hopper <hopperj>
# @Date:   2016-11-01
# @Email:  hopperj@ampereinnotech.com
# @Last modified by:   hopperj
# @Last modified time: 2016-11-03
# @License: GPL3



# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



import pymongo
# import sqlite3
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class GeneralCrawlerPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

        # self.collection.remove( {  } )
        # print("Mongo all set up!")
        # self.connection = sqlite3.connect('frank.db')
        # self.cursor = self.connection.cursor()



    def process_item(self, item, spider):
        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        print('Inserted: ',item['url'])
        return item
