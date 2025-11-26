from unittest.mock import Mock, patch

from src.headHunterAPI import HeadHunterAPI


@patch("requests.get")
def test_get_vacancies(mock_get: Mock, t_api_response: dict) -> None:
    """Тестирование функции получения вакансий из hh.ru"""

    mock_get.return_value.text = t_api_response
    mock_get.return_value.status_code = 200
    hh = HeadHunterAPI()
    assert hh.get_vacancies("Python") == [
        {"id": 1, "linq": "https://www.example.org/one", "name": "one", "salary_from": 1, "salary_to": 2},
        {"id": 2, "linq": "https://www.example.org/two", "name": "two", "salary_from": 2, "salary_to": 3},
        {"id": 3, "linq": "https://www.example.org/tree", "name": "tree", "salary_from": 3, "salary_to": 4},
    ]
