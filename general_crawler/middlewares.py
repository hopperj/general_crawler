# @Author: Jason Hopper <hopperj>
# @Date:   2016-11-03
# @Email:  jason.t.hopper@gmail.com
# @Last modified by:   hopperj
# @Last modified time: 2016-11-03
# @License: GPL3



from scrapy.exceptions import IgnoreRequest
import pymongo
from scrapy.conf import settings

class IgnoreDuplicates():

    def __init__(self):
        self.crawled_urls = set()

        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_request(self, request, spider):
        if self.collection.find({'url':request.url}).count():
            # return 1
            raise IgnoreRequest()
        else:
            return None
