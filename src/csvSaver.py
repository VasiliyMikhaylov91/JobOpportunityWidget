import csv
from src.fileSaver import FileSaver
from src.utils import delete_data, update_data, cast_obj_to_list
from src.vacancy import Vacancy

class CSVSaver(FileSaver):
    """Сохранение и работа с вакансиями в .csv файле"""

    def __init__(self, file_name: str = 'data/vacancies.csv'):
        self.__file_name = file_name

    def save(self, data: list[Vacancy]) -> None:
        """Сохранение вакансий в файл"""

        prepared_data = cast_obj_to_list(data)
        with open(self.__file_name, 'w', newline='') as f:
            fieldnames = ['item_number', 'name', 'linq', 'salary_from', 'salary_to']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            for item in prepared_data:
                writer.writerow(item)

    def get(self) -> list[Vacancy]:
        """Получение вакансий из файла"""

        with open(self.__file_name, 'w', newline='') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        return Vacancy.cast_to_object_list(data)

    def update(self, new_data: Vacancy) -> None:
        """Добавление вакансии или обновление вакансии с таким же id"""

        data = self.get()
        data = update_data(data, new_data)
        self.save(data)

    def delete(self, item_id: int) -> None:
        """Удаление вакансии с таким по id"""

        data = self.get()
        data = delete_data(data, item_id)
        if data == -1:
            return
        self.save(data)
