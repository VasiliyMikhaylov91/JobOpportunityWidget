from abc import ABC, abstractmethod


class JobAPI(ABC):  # pragma: no cover
    """API для получения вакансий"""

    @abstractmethod
    def get_vacancies(self, key_word: str) -> list[dict]:
        pass
