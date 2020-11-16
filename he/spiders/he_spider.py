import scrapy

class HeSpider(scrapy.Spider):
    name = "he_posts"

    start_urls = [
        'https://highexistence.com/meditation-mindfulness/'
    ]

    def parse(self, response):
        for post in response.css('article'):
            yield {
                'title': post.css('h2 a::text').get(),
                'link': post.css('h2 a::attr(href)').get(),
                'text': post.css('.tve-cb section p::text').get(),
                'author': post.css('div.tve-cb > p > a::text').get()
            }
