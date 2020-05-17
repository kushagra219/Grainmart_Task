from requests_html import HTMLSession
from scrapy.selector import Selector

# initialize an HTTP session
session = HTMLSession()

# url to be scraped
url = "https://www.dramexchange.com/"

# GET Request
res = session.get(url)

# Intializing a scrapy selector object
sel = Selector(text=res.text)

# Extracting value from Xpath
value = sel.xpath("//*[@id='tb_NationalDramSpotPrice']/tr[3]/td[5]/text()").get()

# Printing the required value
print(value)