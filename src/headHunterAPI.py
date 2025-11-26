import json

import requests

from src.jobAPI import JobAPI


class HeadHunterAPI(JobAPI):
    """Класс для поиска вакансий на HeadHunter"""

    areas_path = "data/areas.json"
    professional_roles_path = "data/professional_roles.json"
    base_url = "https://api.hh.ru/"

    # def __init__(self) -> None:
    # self.__areas: list[dict] = list(dict())
    #
    # self.get_areas()
    # with open("data/user_settings.json", "r", encoding="utf-8") as f:
    #     user_data = json.load(f)
    # self.__area_id = search_hh_id(self.__areas, "areas", user_data["area"])

    def __hh_request(self, key_word: str) -> dict:  # pragma: no cover
        """Запрос данных из api.hh.ru"""

        response = requests.get(f"{self.base_url}vacancies?" f"per_page=20&" f"text={key_word}")
        if response.status_code == 200:
            return dict(json.loads(response.text))
        return dict()

    def get_vacancies(self, key_word: str = "") -> list[dict]:
        """Вывод данных из api.hh.ru в установленном формате"""

        vacancies = self.__hh_request(key_word)["items"]

        if not vacancies:
            return []

        return [
            {
                "id": int(x["id"]),
                "name": x["name"],
                "linq": x["alternate_url"],
                "salary_from": (
                    int(x["salary"]["from"])
                    if x["salary"] and "from" in x["salary"] and isinstance(x["salary"]["from"], int | str)
                    else None
                ),
                "salary_to": (
                    int(x["salary"]["to"])
                    if x["salary"] and "to" in x["salary"] and isinstance(x["salary"]["to"], int | str)
                    else None
                ),
            }
            for x in vacancies
        ]

    # @classmethod
    # def update_areas(cls) -> None: # pragma: no cover
    #     """Сохранение справочника зон поиска вакансий в документ"""
    #
    #     with open(cls.areas_path, "w", encoding="utf-8") as f:
    #         f.write(requests.get(f"{cls.base_url}areas").text)
    #
    # def get_areas(self) -> None: # pragma: no cover
    #     """Получение списка словарей справочника зон поиска из документа"""
    #
    #     with open(self.areas_path, "r", encoding="utf-8") as f:
    #         self.__areas = json.load(f)
