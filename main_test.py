import scrapy
import json
from scrapy.crawler import CrawlerProcess
curPage = 1
print("enter no of pages")
nPages =  int(input())
class MySpider(scrapy.Spider):
    # Your spider definition
    name = "questions"

    def start_requests(self):
        urls = ["https://stackoverflow.com/questions"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            

    def parse(self, response):
        global curPage, nPages
        
        yield { 'questions' : response.css("a.question-hyperlink::text").getall()}
        next_page = response.css('div.pager.fl a[rel="next"]::attr(href)').get()
        if next_page is not None and curPage<nPages:
            print(next_page)
            curPage+=1
            yield response.follow(next_page, callback=self.parse)
        else:
            return

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json',
})

process.crawl(MySpider)
process.start()
# with open("items.json") as f:
#     data = json.load(f)
#     for i in data:
#         for j in i["questions"]:
#             print(j)