import re
from typing import Optional


class Vacancy(object):
    __slots__ = ("item_number", "name", "linq", "salary_from", "salary_to", "salary_str")

    def __init__(self, item_number: int, name: str, linq: str, salary_from: Optional[int], salary_to: Optional[int]):
        self.__validate_int(item_number)
        self.__validate_name(name)
        self.__validate_linq(linq)
        if salary_from:
            self.__validate_int(salary_from)
        if salary_to:
            self.__validate_int(salary_to)
        self.item_number = item_number
        self.name = name
        self.linq = linq
        self.salary_from = salary_from
        self.salary_to = salary_to
        salary_from_str = f"от {salary_from}" if salary_from else ""
        salary_to_str = f"до {salary_to}" if salary_to else ""
        self.salary_str = f"{salary_from_str} {salary_to_str} руб." if salary_from or salary_to else "Не указана"

    @staticmethod
    def __validate_name(name: str) -> None:
        if not name:
            raise ValueError("Название вакансии не может быть пустым")

    @staticmethod
    def __validate_linq(linq: str) -> None:
        """Валидация ссылки на вакансию"""

        def is_valid_url(url: str) -> bool:
            """Проверяет, является ли строка допустимым URL-адресом."""
            regex = re.compile(
                r"https?://"
                r"([-a-zA-Z0-9@:%._+~#=]{1,256}\.)"
                r"[a-zA-Z0-9()]{1,6}\b"
                r"([-a-zA-Z0-9()@:%_+.~#?&/=]*)"
            )
            return bool(regex.match(url))

        if not is_valid_url(linq):
            raise ValueError("Недопустимая ссылка на вакансию")

    @staticmethod
    def __validate_int(salary: int) -> None:
        if not isinstance(salary, int):
            raise ValueError("Недопустимый тип данных")

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list["Vacancy"]:
        return [cls(x["id"], x["name"], x["linq"], x["salary_from"], x["salary_to"]) for x in vacancies]

    def __str__(self) -> str:
        """Строковое представление вакансии"""

        return f"id: {self.item_number} Название {self.name} З/П: {self.salary_str} {self.linq}"

    def __eq__(self, other):  # type: ignore
        """Сравнение вакансий на строгое равенство"""

        return self.salary_from == other.salary_from

    def __lt__(self, other):  # type: ignore
        """Сравнение вакансий: текущая меньше сравниваемой"""

        return self.salary_from < other.salary_from

    def __gt__(self, other):  # type: ignore
        """Сравнение вакансий: текущая больше сравниваемой"""

        return self.salary_from > other.salary_from

    def __le__(self, other):  # type: ignore
        """Сравнение вакансий: текущая меньше или равна сравниваемой"""

        return self.salary_from <= other.salary_from

    def __ge__(self, other):  # type: ignore
        """Сравнение вакансий: текущая больше или равна сравниваемой"""

        return self.salary_from >= other.salary_from
