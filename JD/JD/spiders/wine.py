# -*- coding: utf-8 -*-
import scrapy
from JD.items import JdItem
from scrapy_splash import SplashRequest

class WineSpider(scrapy.Spider):
	name = 'wine'
	allowed_domains = ['jd.com']

	def start_requests(self):
		script = '''
			function main(splash)
				splash:set_viewport_size(1028, 10000)
				splash:go(splash.args.url)
				local scroll_to = splash:jsfunc("window.scrollTo")
				scroll_to(0, 2000)
				splash:wait(3)
				
				return { 
					html = splash:html() 
				}
			end
				'''
		
		for i in range(1, 101):
			url = 'https://search.jd.com/Search?keyword=%E9%85%92%E7%B1%BB&enc=utf-8&page=' + str(i*2 -1)
			print url
			yield SplashRequest(url, callback=self.parse, meta = {
				'dont_redirect': True,
				'splash':{
					'args': {
						'lua_source':script,'images':0
					},
					'endpoint':'execute',
				}
			})


	def parse(self, response):
		wines = response.xpath('//ul[@class="gl-warp clearfix"]/li/div[@class="gl-i-wrap"]') 
		for wine in wines:

			item = JdItem()
			item['name'] = wine.xpath('./div[@class="p-name p-name-type-2"]/a[@target="_blank"]//em/text()').extract_first()

			print item['name'].strip() 

			yield item
