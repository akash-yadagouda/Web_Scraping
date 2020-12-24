import scrapy 

class QuotoSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        #title = respone.css('title::text').extract()
        #yield {'titletext' : title}

        
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:

            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            yield {
                'title' : title,
                'author' : author,
                'tag' : tag
            }


    

    

    

