# Define my item pipelines here
#
# Don't forget to add my pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import json

class PokPipeline(object):
	def __init__(self):
		self.file = open('items.jl', 'wb')

	def process_item(self, item, spider):
		line = json.dumps(dict(item)) + "\n"
		self.file.write(line)
		return item
