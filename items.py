# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from numpy import unicode


class ProjectItem(scrapy.Item):
    Index_link = scrapy.Field()  # to identify the web's page
    ProductName = scrapy.Field()
    TitleLink = scrapy.Field()
    ImageLink = scrapy.Field()
    NumOfReviews = scrapy.Field()
    Ratings = scrapy.Field()
    ProductPrice = scrapy.Field()
    Dimensions = scrapy.Field()
    Weight = scrapy.Field()
    ASIN = scrapy.Field()
    Model = scrapy.Field()
    BestSellerRank = scrapy.Field()
    DateFirst = scrapy.Field()
    Manufacturer = scrapy.Field()


class ProjectItem2(scrapy.Item):
    ProductName = scrapy.Field()
    NumOfReviews = scrapy.Field()
    Ratings = scrapy.Field()
    ProductPrice = scrapy.Field()
    Dimensions = scrapy.Field()
    Weight = scrapy.Field()
    ASIN = scrapy.Field()
    Model = scrapy.Field()
    BestSellerRank = scrapy.Field()
    DateFirst = scrapy.Field()
    Manufacturer = scrapy.Field()
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
class DemoLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip)
    default_output_processor = TakeFirst()
