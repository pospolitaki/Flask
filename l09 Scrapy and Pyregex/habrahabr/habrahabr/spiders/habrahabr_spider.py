import scrapy
import json
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

url = 'https://habrahabr.ru/users/stopdesign/'
articles = os.path.join(url, 'posts/')

JSON_FILE = 'items.jl'
JSON_FILE_PATH =  os.path.join(os.path.dirname(os.path.abspath(__file__)), JSON_FILE)

class ArticleSpider(scrapy.Spider):
    name = 'habrahabr'
    start_urls = [
        articles,
    ]

    custom_settings = {
        'FEED_FORMAT': 'jl',
        'FEED_URI': JSON_FILE_PATH,
    }



    # def start_requests(self):
    #     urls = [articles]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # follow links to the article
        for href in response.css('h2.post__title a::attr(href)'):
            yield response.follow(href, self.parse_article)

        # follow pagination links
        for href in response.css('li.toggle-menu__item.toggle-menu__item_pagination a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_article(self, response):
        def extract_with_css(query):
            return response.css(query).extract()

        yield {
            'title': extract_with_css('h1.post__title.post__title_full span::text'),
            'text': extract_with_css('div.post__text.post__text-html.js-mediator-article::text'),
        }

def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(ArticleSpider)
    process.start()

    content = ''
    with open(JSON_FILE_PATH) as file:
        content = json.load(file)

    with open('items.txt', mode='w') as file:
        file.write(str(content))
        
if __name__ == '__main__':
    main()

        

    
