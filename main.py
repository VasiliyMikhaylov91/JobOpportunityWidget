from src.headHunterAPI import HeadHunterAPI
from src.vacancy import Vacancy

searcher = HeadHunterAPI()
vacancies = searcher.get_vacancies('Python')
vacancy_list = Vacancy.cast_to_object_list(vacancies)
for item in vacancy_list:
    print(item)