import scrapy



class QuestionsSpider(scrapy.Spider):
    name = "questions"

    def start_requests(self):
        urls = ["https://stackoverflow.com/questions"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            

    def parse(self, response):
        yield { 'questions' : response.css("a.question-hyperlink::text").getall()
                    }
       