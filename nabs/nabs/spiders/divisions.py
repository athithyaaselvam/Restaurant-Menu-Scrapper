# -*- coding: utf-8 -*-
import scrapy
# from scrapy.s/piders import CrawlSpider, Rule
# from scrapy.spiders import CSVFeedSpider
# from scrapy.linkex  tractors import LinkExtractor

class DivisionsSpider(scrapy.Spider):
    name = 'divisions'
    allowed_domains = ['www.nabslink.org']
    # start_urls = ['http://nabslink.org/content/contact-our-state-divisions']

    def start_requests(self):
      urls = [
        'http://nabslink.org/content/contact-our-state-divisions'
      ]
      for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
      for row in response.xpath('//*[@class="table table-striped table-bordered"]//tbody/tr'):
        # print (row)
        yield {
          'State' : row.xpath('td[1]//text()').extract_first(),
          'Student President': row.xpath('td[2]//text()').extract_first(),
          'Phone' : row.xpath('td[3]//text()').extract_first(),
          'Email' : row.xpath('td[4]//text()').extract_first(),
          'Affiliate President' : row.xpath('td[5]//text()').extract_first(),
          'Phone' : row.xpath('td[6]//text()').extract_first(),
          'Email' : row.xpath('td[7]//text()').extract_first()
        }

