# @Author: Jason Hopper <hopperj>
# @Date:   2016-11-01
# @Email:  hopperj@ampereinnotech.com
# @Last modified by:   hopperj
# @Last modified time: 2016-11-02
# @License: GPL3



# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GeneralCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    # html_meta = scrapy.Field()
    # html_headers = scrapy.Field()
    html_body = scrapy.Field()
    html_text = scrapy.Field()
    # plain_text = scrapy.Field()
