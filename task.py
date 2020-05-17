from requests_html import HTMLSession
from scrapy.selector import Selector
from selenium import webdriver

# initialize an HTTP session
driver = webdriver.Firefox()

# url to be scraped
url = "https://www.dramexchange.com/"

# GET Request
driver.get(url)

# # Extracting value from Xpath
value = driver.find_element_by_xpath("//*[@id='tb_NationalDramSpotPrice']/tr[3]/td[5]")

# # Printing the required value
print(value.text)


## SECOND APPROACH USING SCRAPY ##

# # initialize an HTTP session
# session = HTMLSession()

# # url to be scraped
# url = "https://www.dramexchange.com/"

# # GET Request
# res = session.get(url)

# # Intializing a scrapy selector object
# sel = Selector(text=res.text)

# # Extracting value from Xpath
# value = sel.xpath("//*[@id='tb_NationalDramSpotPrice']/tr[3]/td[5]/text()").get()

# # Printing the required value
# print(value)