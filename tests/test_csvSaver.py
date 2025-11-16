import os

from src.csvSaver import CSVSaver
from src.vacancy import Vacancy


def test_save(t_vacancies: list[Vacancy]) -> None:
    """Тестирование записи вакансий в файл"""

    test_csv = CSVSaver("test.csv")
    test_csv.save(t_vacancies)
    with open("test.csv", "r", encoding="utf8") as f:
        assert (
            f.read()
            == """id,name,linq,salary_from,salary_to
1,one,https://www.example.org/one,1,2
2,two,https://www.example.org/two,2,3
3,three,https://www.example.org/three,3,4
"""
        )
    os.remove("test.csv")


def test_get(t_vacancies: list[Vacancy]) -> None:
    """Тестирование получения вакансий из файла"""

    test_csv = CSVSaver("test.csv")
    test_csv.save(t_vacancies)
    assert test_csv.get() == t_vacancies
    os.remove("test.csv")


def test_update(t_vacancies: list[Vacancy]) -> None:
    """Тестирование добавления вакансии в файл"""

    test_csv = CSVSaver("test.csv")
    test_csv.save(t_vacancies)
    vacancy_4 = Vacancy(4, "four", "https://www.example.org/four", 4, 5)
    vacancy_3 = Vacancy(3, "three", "https://www.example.org/three", 9, 10)
    test_csv.update(vacancy_4)
    test_csv.update(vacancy_3)
    with open("test.csv", "r", encoding="utf8") as f:
        assert (
            f.read()
            == """id,name,linq,salary_from,salary_to
1,one,https://www.example.org/one,1,2
2,two,https://www.example.org/two,2,3
3,three,https://www.example.org/three,9,10
4,four,https://www.example.org/four,4,5
"""
        )
    os.remove("test.csv")


def test_delete(t_vacancies: list[Vacancy]) -> None:
    """Тестирование удаления вакансии из файла"""

    test_csv = CSVSaver("test.csv")
    test_csv.save(t_vacancies)
    test_csv.delete(4)
    test_csv.delete(3)
    with open("test.csv", "r", encoding="utf8") as f:
        assert (
            f.read()
            == """id,name,linq,salary_from,salary_to
1,one,https://www.example.org/one,1,2
2,two,https://www.example.org/two,2,3
"""
        )
    os.remove("test.csv")
