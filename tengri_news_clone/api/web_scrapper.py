from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse
from api.enums import *
from api.utils import *


class WebScrapper:
    def __init__(self, url):
        chrome_options = Options()
        chrome_options.add_argument('--headless') 
        self.url = url
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_main_news(self):
        self.driver.get(self.url + 'news/page/5/')
        html = self.driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        return get_news_list(soup)
    
    def search(self, query):
        encoded_query = urllib.parse.quote(query)
        self.driver.get(self.url + f'search/?text={encoded_query}')
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return {
            "query": query,
            "news": get_news_list(soup)
        }


    def close(self):
        self.driver.quit()