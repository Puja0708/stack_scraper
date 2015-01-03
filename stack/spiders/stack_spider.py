from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        #stats = Selector(response).xpath('')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            #item['votes'] = question.xpath(
            	#'//*[@id="question-summary-27758175"]/div[1]/div[2]/div[1]/div/span/text()').extract()[0]
            item['stats'] = question.xpath(
            	'//*[@class="stats"').extract()[0]
            #item['views'] = question.xpath(
            	#'//*[@id="question-summary-27758175"]/div[1]/div[3]/text()').extract()[0]
            yield item