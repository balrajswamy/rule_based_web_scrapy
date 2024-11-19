import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RuleBasedSpiderSpider(CrawlSpider):
    name = "rule_based_spider"
    allowed_domains = ["subslikescript.com"]
    start_urls = ["https://subslikescript.com/movies_letter-X"]

    #rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)
    rules = (Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/li/a")), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_xpaths=('//a[@rel="next"][1]'))),)

    def parse_item(self, response):
        #item = {}
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        #return item
        article = response.xpath('//article[@class="main-article"]')
        article_title = article.xpath("./h1/text()")
        plot = article.xpath("./p/text()")
        #transcript = article.xpath('./div[@class="full-script"]/text()')
        print("article_title:\t",article_title.get())

        yield {"title":article_title.get(),
               "plot": plot.get(),
               #"transcript":transcript.getall(),
               "url": response.url}

