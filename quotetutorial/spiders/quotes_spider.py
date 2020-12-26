import scrapy 
from ..items import QuotetutorialItem

class QuotoSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        #title = respone.css('title::text').extract()
        #yield {'titletext' : title}

        item = QuotetutorialItem()


        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:

            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            item['title'] = title
            item['author'] = author
            item['tag'] = tag

            yield item
        '''
            yield {
                'title' : title,
                'author' : author,
                'tag' : tag
            }
        '''
            

            




    

    

    

