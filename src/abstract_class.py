from abc import ABC, abstractmethod


class WorkInVacancies(ABC):
    """" Абстрактный класс для сохранения данных о вакансии """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancies(self):
        """Абстрактный метод для добавления вакансии в список вакансий"""
        pass

    @abstractmethod
    def getting_data_from_vacancies(self):
        """Абстрактный метод для получения вакансии"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Абстрактный метод для удаления вакансии из файловой структуры"""
        pass
