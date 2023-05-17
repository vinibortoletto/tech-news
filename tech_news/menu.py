from tech_news.scraper import get_tech_news
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
            test = get_tech_news(news_amount)
            sys.stderr.write(test)
