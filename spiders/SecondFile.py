import scrapy
from ..items import *
import pandas as pd
import time
class SecondSpider(scrapy.Spider):
    name = 'SecondSpider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/ref=zg_bs_nav_0',
                  'https://www.amazon.com/Best-Sellers/zgbs/wireless/ref=zg_bs_nav_0'
                  ]  # you can add other links, but in the same domain : amazon.com/*

    def parse(self, response):
        product_quote = response.css('.zg-item')
        for elem in product_quote :
           yield scrapy.Request("https://www.amazon.com"+elem.css('.a-link-normal').css('::attr(href)').get(), callback=self.parse_part, dont_filter=True)
        next_page = response.css('li.a-normal a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_part(self,response):
        items = ProjectItem2()  # our instance of Items (our futur columns in the DB)
        lecture = DemoLoader(item=items, response=response)
        lecture.add_css('ProductName','#productTitle::text')
        lecture.add_css('NumOfReviews','#acrCustomerReviewText ::text')
        lecture.add_css('Ratings','#detailBullets_averageCustomerReviews .a-popover-trigger .a-icon-alt ::text ')
        lecture.add_css('ProductPrice','#priceblock_ourprice ::text')
        lecture.add_css('Dimensions','li:nth-child(2) .a-text-bold+ span ::text')
        lecture.add_css('Weight','.selection::text')
        lecture.add_css('ASIN','li:nth-child(6) .a-text-bold+ span ::text')
        lecture.add_css('Model','li:nth-child(3) .a-text-bold+ span ::text')
        lecture.add_css('BestSellerRank','#detailBullets_feature_div+ .detail-bullet-list .a-list-item span span:nth-child(1) ::text')
        lecture.add_css('DateFirst','li:nth-child(4) .a-text-bold+ span ::text')
        lecture.add_css('Manufacturer','li:nth-child(5) .a-text-bold+ span ::text')
        yield lecture .load_item()