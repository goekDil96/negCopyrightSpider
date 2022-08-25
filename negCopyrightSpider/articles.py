from base64 import encode
from bs4 import BeautifulSoup

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
import psycopg2


from items import NegcopyrightspiderItem, DBItems

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Copyright']
    rules = [Rule(LinkExtractor(allow=r'copyright'), callback='parse_items',
             follow=True)]

    def parse_items(self, response):
        item = DBItems()
        soup = BeautifulSoup(response.body, "html.parser", exclude_encodings= ["ISO-8859-7"])

        list_copyrights= list(set(i for i in soup.get_text().splitlines() if "copyright" in i.lower()))
        for i in list_copyrights:
            item["source"] = response.url
            item["datetime"] = str(datetime.now())
            item["copyright_string"] = i.replace("'", " ")

            yield item