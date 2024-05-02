from abc import ABC, abstractmethod


class VacanciesAbstract(ABC):
    """Абстрактный класс для api hh"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
