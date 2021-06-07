import scrapy
from ..items import *
import pandas as pd
import time
class FileO(scrapy.Spider):
    name = 'PartS'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Pampers-Swaddlers-Disposable-Diapers-SUPPLY/dp/B07DCCP3Y1/ref=zg_bs_baby-products_1?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
      'https://www.amazon.com/Pampers-Wipes-Sensitive-Pop-Top-Packs/dp/B079V67BFW/ref=zg_bs_baby-products_3?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/HUGGIES-Natural-Unscented-Sensitive-Refill/dp/B07MVS998P/ref=zg_bs_baby-products_4?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/WaterWipes-Sensitive-Wipes-Packs-Count/dp/B00INOM4X6/ref=zg_bs_baby-products_5?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/Huggies-Bundle-Overnites-Nighttime-Packaging/dp/B08FPFQCCM/ref=zg_bs_baby-products_6?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/HUGGIES-OverNites-Diapers-Overnight-Packaging/dp/B07MVTDFX1/ref=zg_bs_baby-products_7?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/Huggies-Snug-Diapers-Month-Supply/dp/B0839BLNFV/ref=zg_bs_baby-products_8?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/Huggies-Little-Snugglers-Diapers-Packaging/dp/B07MYW85VT/ref=zg_bs_baby-products_10?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/Luvs-Leakguards-Disposable-Diapers-Newborn/dp/B01EKZO93O/ref=zg_bs_baby-products_11?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6',
                  'https://www.amazon.com/HUGGIES-Simply-Clean-Unscented-Wipes/dp/B078XXN56G/ref=zg_bs_baby-products_13?_encoding=UTF8&psc=1&refRID=85NMNSS5KA8K7J8N9XH6'
                  ]  # you can add other links, but in the same domain : amazon.com/*

    def parse(self, response):  # Scrapy runs this method 2 times (bcs we have two links
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
