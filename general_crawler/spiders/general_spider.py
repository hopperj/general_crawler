# @Author: Jason Hopper <hopperj>
# @Date:   2016-05-09
# @Email:  jason.t.hopper@gmail.com
# @Last modified by:   hopperj
# @Last modified time: 2016-11-02
# @License: GPL3



# -*- coding: utf-8 -*-
import scrapy
from urllib import parse as urlparse
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.htmlparser import HtmlParserLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from general_crawler.items import GeneralCrawlerItem

import json
from bs4 import BeautifulSoup

import lxml.etree
import lxml.html


# BASE_URL = 'http://localhost/'


class GeneralSpider(CrawlSpider):
    name = "general_spider"
    allowed_domains = ["afrg.peas.dal.ca"] # ["localhost"]
    start_urls = (
        'http://afrg.peas.dal.ca/',#'localhost/index.html'
    )

    rules = (
        Rule(LinkExtractor( allow=('//')), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        root = lxml.html.fromstring(response.body)
        html = lxml.html.tostring(root, method="text", encoding='unicode')
        # try:
        #     if response.xpath('//*[@id="toolbar"]'):
        #         print("Skipping a pdf")
        #         return
        # except:
        #     print(response.body)
        #     return
        item = GeneralCrawlerItem()
        item['url'] = response.url
        # item['html_meta'] = json.dumps(response.meta)#.decode('utf-8')
        # item['html_headers'] = response.headers.items()
        try:
            item['html_text'] = response.text#Selector(response).xpath('/')#json.dumps(json.loads(root))
        except:
            pass
        item['html_body'] = response.body#.decode('utf-16')
        print('done parse_items')
        return item
