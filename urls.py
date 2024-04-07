from enum import Enum


MAIN_URL = "https://tengrinews.kz/"
SEARCH_URL = MAIN_URL + "search/?text="
NEWS_EDUCATION = MAIN_URL + "newseducation/"


class News_Category(Enum):
    NEWS_URL = MAIN_URL + "news/"
    NEWS_EDUCATION = MAIN_URL + "newseducation/"
    NEWS_CURIOUS = MAIN_URL + "curious/"
    NEWS_HEALTY = MAIN_URL + "healthy/"

