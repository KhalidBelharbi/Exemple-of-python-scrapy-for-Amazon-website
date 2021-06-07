import scrapy
from ..items import ProjectItem
import pandas as pd
import time
class MySpider(scrapy.Spider):
    name = 'MySpider_ID'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Best-Sellers-Baby/zgbs/baby-products/ref=zg_bs_nav_0',
                  'https://www.amazon.com/Best-Sellers/zgbs/wireless/ref=zg_bs_nav_0'
                  ]  # you can add other links, but in the same domain : amazon.com/*
    list_of_visited_links = start_urls.copy()
    items = ProjectItem()  # our instance of Items (our futur columns in the DB)
    def parse(self, response):  # Scrapy runs this method 2 times (bcs we have two links)

       product_quote = response.css('.zg-item') # the frame of each product
       for elem in product_quote :
           res = [ele for ele in self.list_of_visited_links if (ele is response.url)]
           if not bool(res) :
               self.list_of_visited_links.append(response.url)
           partial_link = "https://www.amazon.com"+elem.css('.a-link-normal').css('::attr(href)').get()
           self.items['Index_link'] = self.list_of_visited_links.index(response.url)
           self.items['ProductName'] = elem.css('.a-spacing-small img').css('::attr(alt)').extract()
           self.items['TitleLink'] = partial_link
           self.items['ImageLink'] = elem.css('.a-spacing-small img').css('::attr(src)').extract()
           self.items['NumOfReviews'] = elem.css('.a-size-small.a-link-normal::text').extract()
           self.items['Ratings'] = elem.css('span.a-icon-alt::text').extract()
           self.items['ProductPrice'] = elem.css('.p13n-sc-price::text').extract()
           yield scrapy.Request(elem.css('.a-link-normal').css('::attr(href)').get(), callback=self.parse_part, dont_filter=True)

       next_page = response.css('li.a-normal a::attr(href)').get()
       if next_page is not None:
           yield response.follow(next_page, callback=self.parse)

    def parse_part(self,response):
        self.items['Dimensions']=''
        self.items['Dimensions'] = response.css('li.nth-child(2) .a-text-bold+ span').css('::text').extract()
        self.items['Weight']=''
        self.items['Weight'] = response.css('#detailBulletsWrapper_feature_div strong').css('::text').extract()
        self.items['ASIN']=''
        self.items['ASIN'] = response.css('li.nth-child(6) .a-text-bold+ span').css('::text').extract()
        self.items['Model']=''
        self.items['Model'] = response.css('li.nth-child(3) .a-text-bold+ span').css('::text').extract()
        self.items['BestSellerRank']=''
        self.items['BestSellerRank'] = response.css('#detailBullets_feature_div+ .detail-bullet-list .a-list-item span span:nth-child(1)').css('::text').extract()
        self.items['DateFirst']=''
        self.items['DateFirst'] = response.css('li.nth-child(4) .a-text-bold+ span').css('::text').extract()
        self.items['Manufacturer']=''
        self.items['Manufacturer'] = response.css('li.nth-child(5) .a-text-bold+ span').css('::text').extract()
