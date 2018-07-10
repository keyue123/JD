# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdPipeline(object):
	def __init__(self):
		print("------------打开爬虫---------------")

	def process_item(self, item, spider):
		with open("wine.txt",'a') as fp:
			fp.write(item['name'].encode("utf8") + '\n')
		return item

	def spider_closed(self, spider):
		print("------------关闭爬虫---------------")
