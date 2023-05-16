from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import MagicMock


# Mocks from @isaacost
@pytest.fixture
def mock_find_news():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia bacana",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 3,
            "summary": "Algo muito bacana aconteceu",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/outra-noticia",
            "title": "Outra notícia",
            "timestamp": "05/04/2021",
            "writer": "Outro escritor",
            "reading_time": 4,
            "summary": "Mais uma notícia interessante",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/novidades/mais-uma-noticia",
            "title": "Mais uma notícia",
            "timestamp": "06/04/2021",
            "writer": "Escritor Anônimo",
            "reading_time": 10,
            "summary": "Uma notícia importante",
            "category": "Ciência",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-do-dia",
            "title": "Notícia do dia",
            "timestamp": "07/04/2021",
            "writer": "Mais um escritor",
            "reading_time": 12,
            "summary": "A notícia mais importante do dia",
            "category": "Política",
        },
        {
            "url": "https://blog.betrybe.com/novidades/ultima-noticia",
            "title": "Última notícia",
            "timestamp": "08/04/2021",
            "writer": "Escritor famoso",
            "reading_time": 15,
            "summary": "A última notícia do mês",
            "category": "Entretenimento",
        },
    ]


@pytest.fixture
def mock_output():
    return {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    ("Notícia bacana", 3),
                    ("Outra notícia", 4),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    ("Mais uma notícia", 10),
                ],
            },
        ],
        "unreadable": [
            ("Notícia do dia", 12),
            ("Última notícia", 15),
        ],
    }


def test_reading_plan_group_news(mock_find_news, mock_output):
    error_message = "Valor 'available_time' deve ser maior que zero"

    with pytest.raises(ValueError, match=error_message):
        ReadingPlanService.group_news_for_available_time(0)

    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_find_news)
    assert ReadingPlanService.group_news_for_available_time(10) == mock_output
