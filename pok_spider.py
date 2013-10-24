# encoding: utf-8
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from pok.items import PokItem ##This is the item I defined in items.py

class MySpider(CrawlSpider):
	name='google'
	domain_name = 'google'
	allowed_domains = ['google.hu']
	start_urls = ['https://www.google.hu/&q=pok']
	rules = (Rule (SgmlLinkExtractor(allow=('next\.html', ),restrict_xpaths=('//div[@id="pg"]',)), callback='parse_item', follow= True),)
	
	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		sites= hxs.select('//*[@id="rso"]')
		items =[]
		
		for site in sites:
			item = PokItem() ### this is the item object I defined in the items file
			item["title"] = item.select('/li[1]/div/h3/a/em').extract() ### assuming my item object has “title” field
			sitem["url"] = item.select('/li[1]/div/div/div/div[1]/cite').extract()
			item["desc"] = item.select('/li[1]/div/div/div/span').extract()			
			items.append(item)
		return(items)


