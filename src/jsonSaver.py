import json

from src.fileSaver import FileSaver
from src.utils import cast_obj_to_list, update_data, delete_data
from src.vacancy import Vacancy

class JsonSaver(FileSaver):
    """Сохранение и работа с вакансиями в .json файле"""

    def __init__(self, file_path: str = 'data/vacancies.json'):
        self.__file_name = file_path

    def get(self) -> list[Vacancy]:
        """Получение вакансий из файла"""

        with open(self.__file_name, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        return Vacancy.cast_to_object_list(data)

    def save(self, data: list[Vacancy]) -> None:
        """Сохранение вакансий в файл"""

        data_prepared = cast_obj_to_list(data)
        with open(self.__file_name, 'w', encoding='utf-8') as f:
            json.dumps(data_prepared)

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
