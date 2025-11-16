import pytest

from src.vacancy import Vacancy

# @pytest.fixture
# def ides() -> list[dict]:
#     return [{'id': 1, 'name': 'one', 'box':[{'id': 4, 'name': 'four', 'box':[{'id': 5, 'name': 'five', 'box':[]}]}]},
#             {'id': 2, 'name': 'two', 'box':[]},
#             {'id': 3, 'name': 'three', 'box':[]}]


@pytest.fixture
def t_vacancies() -> list[Vacancy]:
    """Список тестовых вакансий"""

    return [
        Vacancy(1, "one", "https://www.example.org/one", 1, 2),
        Vacancy(2, "two", "https://www.example.org/two", 2, 3),
        Vacancy(3, "three", "https://www.example.org/three", 3, 4),
    ]


@pytest.fixture
def t_api_response() -> str:
    """Тестовый ответ от API hh.ru"""

    return (
        '{"items":['
        '{"id": "1", "name": "one", "alternate_url": "https://www.example.org/one", '
        '"salary": {"from": "1", "to": "2"}},'
        '{"id": "2", "name": "two", "alternate_url": "https://www.example.org/two", '
        '"salary": {"from": "2", "to": "3"}},'
        '{"id": "3", "name": "tree", "alternate_url": "https://www.example.org/tree", '
        '"salary": {"from": "3", "to": "4"}}'
        "]}"
    )
