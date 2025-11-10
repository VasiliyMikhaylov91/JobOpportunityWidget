from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class FileSaver(ABC):
    """Работа с вакансиями сохраненными в файле"""

    @abstractmethod
    def get(self) -> list[Vacancy]:
        """Получение вакансий из файла"""
        pass

    @abstractmethod
    def update(self, data: Vacancy) -> None:
        """Добавление вакансии или обновление вакансии с таким же id"""
        pass

    @abstractmethod
    def delete(self, vacancy_id: int) -> None:
        """Удаление вакансии с таким по id"""
        pass