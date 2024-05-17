import json
from abstract_work_with_data import WorkInVacancies
from src.vacancies import VacanciesHH

class SavedVacancies(WorkInVacancies):
    """Класс для сохранения данных о вакансии в JSON-файл"""
    file_with_vacancies = "file_with_vacancies.json"
    vacancies = []

    def add_vacancy(self, vacancy: VacanciesHH):
        """Метод для добавления вакансии в список вакансий"""
        if isinstance(vacancy, VacanciesHH):
            vacancy_dict = {'name': vacancy.name, 'url': vacancy.url,
                            'salary': vacancy.get_salary,
                            'requirements': vacancy.requirements}
            self.vacancies.append(vacancy_dict)
        else:
            raise ValueError("Должен быть передан объект класса Vacancy!")


    def add_vacancies_in_json(self):
        """Метод для добавления вакансии в JSON-файл"""
        with open(self.file_with_vacancies, "w") as file:
            json.dump(self.vacancies, file)


    def get_vacancies(self, name_of_vacancy: str) -> dict:
        """Метод для получения вакансии"""
        for vacancy in self.vacancies:
            if vacancy['name'] == name_of_vacancy:
                return VacanciesHH(vacancy['name'], vacancy['url'], vacancy['salary'],
                               vacancy['requirements'])


    def delete_vacancy(self,vacancy: VacanciesHH):
        """Метод для удаления вакансии из JSON-файла"""

        dict_to_remove = {'name': vacancy.name, 'url': vacancy.url,
                          'salary': vacancy.get_salary,
                          'requirements': vacancy.requirements}

        self.vacancies.remove(dict_to_remove)

        with open(self.file_with_vacancies, 'w') as file:
            json.dump(self.vacancies, file)


# json_saver = SavedJSON()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)
