from django.shortcuts import render
from api.web_scrapper import WebScrapper
from api.enums import News_Category
from api.utils import html_news_to_model

# Create your views here.
def test_news(request): 
    chrome_scrapper = WebScrapper(News_Category.MAIN_URL.value)

    news_list = chrome_scrapper.get_main_news()
    chrome_scrapper.close()

    news_presentation = []
    for news_item in news_list:
        news_presentation.append(html_news_to_model(news_item))


    return render(request, "index.html", {"input": news_presentation})

