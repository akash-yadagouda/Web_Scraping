import scrapy 

class QuotoSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'http://kletech.ac.in/'
    ]

    def parse(self, respone):
        title = respone.css('title::text').extract()
        yield {'titletext' : title}

    

    

