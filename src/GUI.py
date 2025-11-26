from src.csvSaver import CSVSaver
from src.headHunterAPI import HeadHunterAPI
from src.jsonSaver import JsonSaver
from src.vacancy import Vacancy


def hh_script() -> None:  # pragma: no cover
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = HeadHunterAPI()
    vacancies = Vacancy.cast_to_object_list(hh_vacancies.get_vacancies(search_query))
    for vacancy in vacancies:
        print(vacancy)
    save_to_file = input("Сохранить в файл? 1 - json файл; 2 - csv файл; 3 - не сохранять -> ")
    if save_to_file == "1" or save_to_file == "2":
        saver = JsonSaver() if save_to_file == "1" else CSVSaver()
        saver.save(vacancies)  # type: ignore


def file_script(file_type: str) -> None:  # pragma: no cover
    saver = JsonSaver() if file_type == "json" else CSVSaver()
    vacancies = saver.get()  # type: ignore
    for vacancy in vacancies:
        print(vacancy)
    option = input("1 - Добавить/Изменить вакансию; 2 - Удалить вакансию -> ")
    if option == "1":
        vacancy_id = int(
            input(
                "Введите новый id вакансии для добавления новой \n"
                "или имеющийся для изменения существующей вакансии -> "
            )
        )
        vacancy_name = input("Введите название вакансии -> ")
        vacancy_linq = input("Ссылка на вакансию -> ")
        vacancy_salary_from = int(input("Зарплата от -> "))
        vacancy_salary_to = int(input("Зарплата до -> "))
        saver.update(
            Vacancy(vacancy_id, vacancy_name, vacancy_linq, vacancy_salary_from, vacancy_salary_to)  # type: ignore
        )
    elif option == "2":
        vacancy_id = int(input("Укажите id для удаления -> "))
        saver.delete(vacancy_id)  # type: ignore


def user_interaction() -> None:  # pragma: no cover
    vacancy_source = input("Выберите источник вакансий 1 - hh.ru; 2 - json файл; 3 - csv файл -> ")
    if vacancy_source == "1":
        hh_script()
    elif vacancy_source == "2":
        file_script("json")
    elif vacancy_source == "3":
        file_script("csv")
