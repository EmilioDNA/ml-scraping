# Impoorting all the required modules
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

# Create a class that extends the Item, included the desired fields
class Product(Item):
    title = Field()
    price = Field()
    description = Field()

# Create a class that extends from CrawlSpider, it's responsible for running the general crawler
class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadoLibre' # name of the crawler
    # Include user agents to avoid detection (at least to try) and also specified the number of limit items to crawl.
    custom_settings = { 
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64)\
                        AppleWebKit/537.36 (KHTML, like Gecko)\
                        Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 40

    }
    # these are the main domains allowed for this example
    allowed_domains = ['listado.mercadolibre.com.mx', 'mercadolibre.com.mx']
    # the pet category was chosen, this is the seed url
    start_urls = ['https://listado.mercadolibre.com.mx/animales/perros/']
    # Try to delay the request each second
    download_delay = 1
    # General rules for the crawler
    rules = (
        Rule( # This rule evaluates the seed url horizontally but it doesn't get any data, it allows the pagination
            LinkExtractor(
                allow=r'/_Desde_\d+' # key identifier of the url for this category
            ), follow=True),
        Rule( # This rule evaluate the urls vertically in depth in order to get the full detail of each item/website
            LinkExtractor(
                allow=r'/MLM-' # key identifier of the url of the details page
            ), follow=True, callback='parse_items'),
    )
    # This is the callback function that gets the data and parse it
    def parse_items(self, response):
        item = ItemLoader(Product(), response)
        # The title and description are included using xpath to get the elements and are formatted with an anonymous lambda function
        item.add_xpath('title', '//h1/text()', MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        item.add_xpath('description', '//div[@class="item-description__text"]/p/text()',
                       MapCompose(lambda i: i.replace('\n', ' ').replace('\r', ' ').strip()))
        # In the other hand, I used Beautiful Soup to get the price and format it before add it to the class instance 
        soup = BeautifulSoup(response.body)
        price = soup.find(class_="price-tag")
        full_price = price.text.replace('\n', ' ').replace('\r', ' ').replace(' ', '')
        item.add_value('price', full_price)
        # A yield to perform the full operation for each instance of the classes
        yield item.load_item()
