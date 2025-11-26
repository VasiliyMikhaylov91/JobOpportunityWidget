from abc import ABC, abstractmethod
from typing import Union

from src.vacancy import Vacancy


class FileSaver(ABC):  # pragma: no cover
    """Работа с вакансиями сохраненными в файле"""

    @abstractmethod
    def get(self) -> list[Vacancy]:
        """Получение вакансий из файла"""
        pass

    def save(self, data: Union[list[Vacancy], int]) -> None:
        """Сохранение данных в файл"""
        pass

    @abstractmethod
    def update(self, data: Vacancy) -> None:
        """Добавление вакансии или обновление вакансии с таким же id"""
        pass

    @abstractmethod
    def delete(self, vacancy_id: int) -> None:
        """Удаление вакансии с таким по id"""
        pass
