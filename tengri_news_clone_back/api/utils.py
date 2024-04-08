from bs4 import BeautifulSoup
import dateparser
from api.enums import News_Category
from api.models import News
import datetime
import locale

def get_news_list(soup: BeautifulSoup):
    rubric = soup.find("div", class_="content rubric")
    if rubric == None:
        return []
    main_news = rubric.find("div", class_="content_main")
    news_items = main_news.find_all("div", class_="content_main_item")

    return news_items

def html_news_to_model(news_item: BeautifulSoup):
    title = news_item.find("span", "content_main_item_title").text.strip()
    content = news_item.find("span", "content_main_item_announce").text.strip()
    img = News_Category.MAIN_URL.value + news_item.find("img", "content_main_item_img")['src'].strip()
    url = News_Category.MAIN_URL.value + news_item.find("a")['href']
    date = news_item.find("div", "content_main_item_meta").find("span", class_=False).text.strip()
    formatted_date = convert_date(date)
    return News(title=title, url=url, content=content, img=img, date=formatted_date)


def convert_date(date: str): 
    if date.lower() == 'сегодня':
        return datetime.datetime.today()
    elif date.lower() == 'вчера':
        return datetime.datetime.today() - datetime.timedelta(days=1)
    
    date_object = dateparser.parse(date, languages=['ru'])
    return date_object.date()

    

def format_date(date: datetime):
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
    formatted_date = date.strftime('%d %B %Y')

    return formatted_date
