class VacanciesHH():
    """Класс для работы с вакансиями"""

    def __init__(self, name: str, url: str, salary: float, requirements: str):
        """Конструктор класса VacanciesHH"""
        if not name:
            raise ValueError("Название вакансии должно быть указано!")
        self.name = name

        if not url:
            raise ValueError("URL-адрес вакансии должен быть указан!")
        self.url = url

        self.__salary = salary

        if requirements == "None":
            self.requirements = "Требования не указаны"
        self.requirements = requirements

    @property
    def get_salary(self) -> float:
        """Геттер для зарплаты"""
        return self.__salary

    def __ge__(self, other) -> bool:
        """Магический метод для cравнения вакансий по зарплате"""
        return self.__salary >= other.__salary

    def __repr__(self) -> str:
        """Магический метод для отображения созданного экземпляра класса Vacancy"""

        return f"Vacancy('{self.name}', '{self.url}', {self.__salary}, '{self.requirements}')"

    def __str__(self):
        if self.__salary is None:
            return f"Название: {self.name}, зарплата не указана, требования: {self.requirements}, ссылка: {self.url}"

        return f"Название: {self.name}, зарплата: {self.__salary}, требования: {self.requirements}, ссылка: {self.url}"
