from tech_news.database import search_news
from datetime import datetime


def transform_list_into_dict(list):
    return [(news["title"], news["url"]) for news in list]


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news_list = search_news(query)
    return transform_list_into_dict(news_list)


# Requisito 8
def search_by_date(date):
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")

    unformatted_date = datetime.strptime(date, "%Y-%m-%d")
    formatted_date = datetime.strftime(unformatted_date, "%d/%m/%Y")

    query = {"timestamp": formatted_date}
    news_list = search_news(query)
    return transform_list_into_dict(news_list)


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news_list = search_news(query)
    return transform_list_into_dict(news_list)
