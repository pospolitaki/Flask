import scrapy
import os
import json
import pprint
from scrapy.crawler import CrawlerProcess

url = 'https://habrahabr.ru/users/s_a_p/posts/'
JSON_FILE = 'items.json'
JSON_FILE_PATH =  os.path.join(os.path.dirname(os.path.abspath(__file__)), JSON_FILE)


class UserArticlesSpider(scrapy.Spider):
    name = "user_articles"

    start_urls = [
        url,
        
    ]

    custom_settings = {
        'FEED_FORMAT': 'jl',
        'FEED_URI': JSON_FILE_PATH,
    }

    def parse(self, response):
        # follow links to author publications
        css_queries = [
            'a.btn.btn_x-large.btn_outline_blue.post__habracut-btn::attr(href)',
            'a.post__title_link::attr(href)',            
        ]
        for query in css_queries:
            for href in response.css(query):
                yield response.follow(href, self.parse_user_articles)

        css_query = 'a.arrows-pagination__item-link.arrows-pagination__item-link_next::attr(href)'
        for href in response.css(css_query):
            yield response.follow(href, self.parse)

    def parse_user_articles(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first()

        yield {
            # 'name': extract_with_css('h3.author-title::text'),
            # 'birthdate': extract_with_css('.author-born-date::text'),
            # 'bio': extract_with_css('.author-description::text'),
            # 'url': response.url,
            'title': extract_with_css('span.post__title-text::text'),
            # 'article':  extract_with_css('div.post__body.post__body_full'),
        }
    
def main():
    if os.path.isfile(JSON_FILE_PATH):
        os.remove(JSON_FILE_PATH)

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(UserArticlesSpider)
    process.start()

    content = ''
    with open(JSON_FILE_PATH) as f:
        content = json.load(f)
    
    with open('items.html', 'w') as f:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(content)
        f.write(str(content))

if __name__ == '__main__':
    main()
