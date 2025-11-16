from src.utils import cast_obj_to_list, delete_data, update_data
from src.vacancy import Vacancy

# def test_search_hh_id(ides: list[dict]) -> None:
#     assert 5 == search_hh_id(ides, 'box', 'five')
#     assert 3 == search_hh_id(ides, 'box', 'three')


def test_update_data(t_vacancies: list[Vacancy]) -> None:
    """Тестирование добавления вакансии в список вакансий"""

    new_vacancy_1 = Vacancy(1, "one", "https://www.example.org/one", 6, 8)
    new_vacancy_2 = Vacancy(6, "six", "https://www.example.org/six", 7, 9)
    assert update_data(t_vacancies, new_vacancy_1) == [
        Vacancy(1, "one", "https://www.example.org/one", 6, 8),
        Vacancy(2, "two", "https://www.example.org/two", 2, 3),
        Vacancy(3, "three", "https://www.example.org/three", 3, 4),
    ]
    assert update_data(t_vacancies, new_vacancy_2) == [
        Vacancy(1, "one", "https://www.example.org/one", 6, 8),
        Vacancy(2, "two", "https://www.example.org/two", 2, 3),
        Vacancy(3, "three", "https://www.example.org/three", 3, 4),
        Vacancy(6, "six", "https://www.example.org/six", 7, 9),
    ]


def test_delete_data(t_vacancies: list[Vacancy]) -> None:
    """Тестирование удаления вакансии из списка вакансий"""

    assert delete_data(t_vacancies, 1) == [
        Vacancy(2, "two", "https://www.example.org/two", 2, 3),
        Vacancy(3, "three", "https://www.example.org/three", 3, 4),
    ]
    assert -1 == delete_data(t_vacancies, 8)


def test_cast_obj_to_list(t_vacancies: list[Vacancy]) -> None:
    """Тестирование преобразования списка вакансий в список словарей"""

    assert (
        cast_obj_to_list(t_vacancies)
        == [
            {"id": 1, "linq": "https://www.example.org/one", "name": "one", "salary_from": 1, "salary_to": 2},
            {"id": 2, "linq": "https://www.example.org/two", "name": "two", "salary_from": 2, "salary_to": 3},
            {"id": 3, "linq": "https://www.example.org/three", "name": "three", "salary_from": 3, "salary_to": 4},
        ]
        != [{}]
    )
