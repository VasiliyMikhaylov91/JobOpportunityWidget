import os

from src.jsonSaver import JsonSaver
from src.vacancy import Vacancy


def test_save(t_vacancies: list[Vacancy]) -> None:
    """Тестирование записи вакансий в файл"""

    test_json = JsonSaver("test.json")
    test_json.save(t_vacancies)
    with open("test.json", "r") as f:
        assert f.read() == (
            '[{"id": 1, "name": "one", "linq": "https://www.example.org/one", '
            '"salary_from": 1, "salary_to": 2}, {"id": 2, "name": "two", "linq": '
            '"https://www.example.org/two", "salary_from": 2, "salary_to": 3}, {"id": 3, '
            '"name": "three", "linq": "https://www.example.org/three", "salary_from": 3, '
            '"salary_to": 4}]'
        )
    os.remove("test.json")


def test_get(t_vacancies: list[Vacancy]) -> None:
    """Тестирование получения вакансий из файла"""

    test_json = JsonSaver("test.json")
    test_json.save(t_vacancies)
    assert test_json.get() == t_vacancies
    os.remove("test.json")


def test_update(t_vacancies: list[Vacancy]) -> None:
    """Тестирование добавления вакансии в файл"""

    test_json = JsonSaver("test.json")
    test_json.save(t_vacancies)
    vacancy_4 = Vacancy(4, "four", "https://www.example.org/four", 4, 5)
    vacancy_3 = Vacancy(3, "three", "https://www.example.org/three", 9, 10)
    test_json.update(vacancy_4)
    test_json.update(vacancy_3)
    with open("test.json", "r", encoding="utf8") as f:
        assert f.read() == (
            '[{"id": 1, "name": "one", "linq": "https://www.example.org/one", '
            '"salary_from": 1, "salary_to": 2}, {"id": 2, "name": "two", "linq": '
            '"https://www.example.org/two", "salary_from": 2, "salary_to": 3}, {"id": 3, '
            '"name": "three", "linq": "https://www.example.org/three", "salary_from": 9, '
            '"salary_to": 10}, {"id": 4, "name": "four", "linq": '
            '"https://www.example.org/four", "salary_from": 4, "salary_to": 5}]'
        )
    os.remove("test.json")


def test_delete(t_vacancies: list[Vacancy]) -> None:
    """Тестирование удаления вакансии из файла"""

    test_json = JsonSaver("test.json")
    test_json.save(t_vacancies)
    test_json.delete(4)
    test_json.delete(3)
    with open("test.json", "r", encoding="utf8") as f:
        assert f.read() == (
            '[{"id": 1, "name": "one", "linq": "https://www.example.org/one", '
            '"salary_from": 1, "salary_to": 2}, {"id": 2, "name": "two", "linq": '
            '"https://www.example.org/two", "salary_from": 2, "salary_to": 3}]'
        )
    os.remove("test.json")
