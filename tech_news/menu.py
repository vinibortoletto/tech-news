from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
import sys


# Requisitos 11 e 12
def analyzer_menu():
    options_message = (
        "Selecione uma das opções a seguir: \n"
        "0 - Popular o banco com notícias; \n"
        "1 - Buscar notícias por título; \n"
        "2 - Buscar notícias por data; \n"
        "3 - Buscar notícias por categoria; \n"
        "4 - Listar top 5 categorias; \n"
        "5 - Sair. \n"
    )

    try:
        selected_option = int(input(options_message))
    except ValueError:
        sys.stderr.write("Opção inválida")
    else:
        if selected_option == 0:
            news_amount = int(input("Digite quantas notícias serão buscadas:"))
            news_list = get_tech_news(news_amount)
            sys.stderr.write(str(news_list))

        elif selected_option == 1:
            news_title = input("Digite o título:")
            news_list = search_by_title(news_title)
            sys.stderr.write(str(news_list))

        elif selected_option == 2:
            news_date = input("Digite a data no formato aaaa-mm-dd:")
            news_list = search_by_date(news_date)
            sys.stderr.write(str(news_list))

        elif selected_option == 3:
            news_category = input("Digite a categoria:")
            news_list = search_by_category(news_category)
            sys.stderr.write(str(news_list))
