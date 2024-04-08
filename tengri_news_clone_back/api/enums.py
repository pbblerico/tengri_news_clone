from enum import Enum

class News_Category(Enum):
    MAIN_URL = "https://tengrinews.kz/"
    NEWS_URL = MAIN_URL + "news/"
    SEARCH_URL = MAIN_URL + "search/?text="
    NEWS_EDUCATION = MAIN_URL + "newseducation/"
    NEWS_CURIOUS = MAIN_URL + "curious/"
    NEWS_HEALTY = MAIN_URL + "healthy/"
