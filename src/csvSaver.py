import csv
from typing import Union

from src.fileSaver import FileSaver
from src.utils import cast_obj_to_list, delete_data, update_data
from src.vacancy import Vacancy


class CSVSaver(FileSaver):
    """Сохранение и работа с вакансиями в .csv файле"""

    def __init__(self, file_name: str = "data/vacancies.csv"):
        self.__file_name = file_name

    def save(self, data: Union[list[Vacancy], int]) -> None:
        """Сохранение вакансий в файл"""

        if isinstance(data, int):
            return
        prepared_data = cast_obj_to_list(data)
        with open(self.__file_name, "w", newline="") as f:
            fieldnames = ["id", "name", "linq", "salary_from", "salary_to"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for item in prepared_data:
                writer.writerow(item)

    def get(self) -> list[Vacancy]:
        """Получение вакансий из файла"""

        with open(self.__file_name, "r", newline="") as f:
            reader = csv.DictReader(f)
            data_read = [row for row in reader]
        data = [
            {
                "id": int(x["id"]),
                "name": x["name"],
                "linq": x["linq"],
                "salary_from": (
                    int(x["salary_from"]) if x["salary_from"] and isinstance(x["salary_from"], int | str) else None
                ),
                "salary_to": (
                    int(x["salary_to"]) if x["salary_to"] and isinstance(x["salary_from"], int | str) else None
                ),
            }
            for x in data_read
        ]
        return Vacancy.cast_to_object_list(data)

    def update(self, new_data: Vacancy) -> None:
        """Добавление вакансии или обновление вакансии с таким же id"""

        data = self.get()
        data = update_data(data, new_data)
        self.save(data)

    def delete(self, item_id: int) -> None:
        """Удаление вакансии с таким по id"""

        data = self.get()
        data_new = delete_data(data, item_id)
        self.save(data_new)
