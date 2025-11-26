import pytest

from src.vacancy import Vacancy


def test_validation() -> None:
    """Тестирование валидации входных переменных создания вакансии"""

    with pytest.raises(ValueError):
        Vacancy("1", "one", "https://www.example.org/one", 1, 2)  # type: ignore
    with pytest.raises(ValueError):
        Vacancy(2, "", "https://www.example.org/two", 2, 3)
    with pytest.raises(ValueError):
        Vacancy(3, "tree", "www.example.org/three", 3, 4)
    with pytest.raises(ValueError):
        Vacancy(3, "tree", "https://www.example.org/three", "3", 4)  # type: ignore
    with pytest.raises(ValueError):
        Vacancy(3, "tree", "https://www.example.org/three", 3, "5")  # type: ignore


def test_vacancy_str() -> None:
    """Тестирование строкового представления вакансии"""

    assert (
        str(Vacancy(2, "two", "https://www.example.org/two", 2, 3))
        == "id: 2 Название two З/П: от 2 до 3 руб. https://www.example.org/two"
    )


def test_vacancy_eq() -> None:
    """Тестирование вакансий на равенство"""

    v1 = Vacancy(2, "two", "https://www.example.org/two", 2, 3)
    v2 = Vacancy(3, "three", "https://www.example.org/three", 2, 4)
    assert v1 == v2


def test_vacancy_ne() -> None:
    """Тестирование вакансий на неравенство"""

    v1 = Vacancy(2, "two", "https://www.example.org/two", 2, 3)
    v2 = Vacancy(3, "three", "https://www.example.org/three", 3, 4)
    assert v1 != v2


def test_vacancy_le() -> None:
    """Тестирование вакансий на меньше или равно"""

    v1 = Vacancy(2, "two", "https://www.example.org/two", 2, 3)
    v2 = Vacancy(3, "three", "https://www.example.org/three", 3, 4)
    assert v1 <= v2


def test_vacancy_ge() -> None:
    """Тестирование вакансий на больше или равно"""

    v1 = Vacancy(2, "two", "https://www.example.org/two", 2, 3)
    v2 = Vacancy(3, "three", "https://www.example.org/three", 3, 4)
    assert v2 >= v1


def test_vacancy_lt() -> None:
    """Тестирование вакансий на меньше"""

    v1 = Vacancy(2, "two", "https://www.example.org/two", 2, 3)
    v2 = Vacancy(3, "three", "https://www.example.org/three", 3, 4)
    assert v1 < v2


def test_vacancy_gt() -> None:
    """Тестирование вакансий на больше"""

    v1 = Vacancy(2, "two", "https://www.example.org/two", 2, 3)
    v2 = Vacancy(3, "three", "https://www.example.org/three", 3, 4)
    assert v2 > v1
