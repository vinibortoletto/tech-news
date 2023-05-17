from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news_list = find_news()
    category_ranking_dict = dict()

    for news in news_list:
        category = news["category"]

        if category not in category_ranking_dict:
            category_ranking_dict[f"{category}"] = 1
        else:
            category_ranking_dict[f"{category}"] += 1

    category_ranking_list = list(
        sorted(
            category_ranking_dict.items(),
            key=lambda x: (-x[1], x[0]),
        )
    )

    category_ranking_list = [category[0] for category in category_ranking_list]

    return category_ranking_list[:5]
