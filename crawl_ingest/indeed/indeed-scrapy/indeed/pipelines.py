# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo.mongo_client import MongoClient

class MongoDBPipeline:
    collection_name = 'indeed'
    ingest_collection_name = 'merged_collections'
    def open_spider(self,spider) :
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["jobs"]
        
    def close_spider(self,spider):
        self.client.close()
    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        self.db[self.ingest_collection_name].insert(self.process_for_ingest(item))
        return item
    def process_for_ingest(self,item):
        raise NotImplementedError
    
class IndeedPipeline:
    def process_item(self, item, spider):
        return item
