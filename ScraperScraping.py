from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import time
def scrapeInternetLink():
    global text
    #this opens up the website in my firefox and reads all the info from it then closes it
    driver = webdriver.Firefox(options = Options())
    driver.get("http://neumont.smartcatalogiq.com/2021-2022/Catalog/Academic-Calendar")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    text = soup.get_text()
    return text