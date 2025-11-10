from src.vacancy import Vacancy

def search_hh_id(collection: list[dict], collection_name: str, name: str) -> int |None:
    """Рекурсивный поиск id по названию в справочнике collection. collection_name имя вложенных списков"""

    for item in collection:
        if item['name'] == name:
            return item['id']
        if collection_name in item:
            item_id = search_hh_id(item[collection_name], collection_name,name)
            if item_id:
                return item_id
    return None

def update_data(data: list[Vacancy], new_data: Vacancy) -> list[Vacancy]:
    """Обновление списка вакансий при добавлении новой вакансии"""
    for i in range(len(data)):
        if data[i].item_number == new_data.item_number:
            data[i] = new_data
            break
    else:
        data.append(new_data)
    return data

def delete_data(data: list[Vacancy], item_id: int) -> list[Vacancy] | int:
    """Удаление вакансии из списка"""

    for i in range(len(data)):
        if data[i].item_number == item_id:
            data.pop(i)
            break
    else:
        return -1
    return data

def cast_obj_to_list(data: list[Vacancy]) -> list[dict]:

    return [{'id': x.item_number,
             'name': x.name,
             'linq': x.linq,
             'salary_from': x.salary_from,
             'salary_to': x.salary_to}
            for x in data]