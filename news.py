from bs4 import BeautifulSoup

def get_news_list(soup: BeautifulSoup):
    rubric = soup.find("div", class_="content rubric")
    if rubric == None:
        return []
    main_news = rubric.find("div", class_="content_main")
    # if main_news == None:
    #     return 0
    news_items = main_news.find_all("div", class_="content_main_item")

    return news_items