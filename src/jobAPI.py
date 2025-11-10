from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JobAPI(ABC):
    """API для получения вакансий"""

    @abstractmethod
    def get_vacancies(self, key_word: str) -> list[Vacancy]:
        pass