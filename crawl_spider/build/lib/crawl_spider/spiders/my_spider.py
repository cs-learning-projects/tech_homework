import json
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from crawl_spider.items import CrawlSpiderItem
from scrapy.linkextractors import LinkExtractor


class MyCrawlSpider(CrawlSpider):
    name = 'my_spider'
    allowed_domains = ['habrahabr.ru']
    start_urls = ['https://habrahabr.ru/']

    rules = Rule(LinkExtractor(allow=('https://habrahabr.ru/post/.*')), callback='parse_items', follow=True),
    # почему в конце нужна запятая?? Без нее не работает

    def parse_items(self, response):
        item = CrawlSpiderItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1[@class="post__title"]/span/text()').extract()
        item['text'] = response.xpath('normalize-space(//div[@class="content html_format"])').extract()
        item['hab'] = response.xpath('//div[@class="hubs"]/a/text()').extract()
        # json_output_file = open('output.json', 'a')
        # json_output_file.write(json.dumps(dict(item), ensure_ascii=False))
        # json_output_file.close()
        return item

