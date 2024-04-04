from colorama import *


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name_vacs, url_vacs, city_vacs, desc_vacs, salary_vacs, requirement_vacs):
        self.name_vacs = name_vacs
        self.url_vacs = url_vacs
        self.city_vacs = city_vacs
        self.desc_vacs = desc_vacs
        self.salary_vacs = salary_vacs
        self.requirement_vacs = requirement_vacs

    def __repr__(self):
        return (f"{self.name_vacs} {self.url_vacs} {self.city_vacs} {self.desc_vacs} {self.salary_vacs} "
                f"{self.requirement_vacs}")

    def __str__(self):
        return (f'Вакансия: {Fore.LIGHTYELLOW_EX}{self.name}{Fore.RESET}\n'
                f'Ссылка: {Fore.LIGHTGREEN_EX}{self.url}{Fore.RESET}\n'
                f'Город: {Fore.LIGHTGREEN_EX}{self.city}{Fore.RESET}\n'
                f'Описание: {Fore.LIGHTYELLOW_EX}{self.desc}{Fore.RESET}\n'
                f'Зарплата: {Fore.LIGHTGREEN_EX}{self.salary}{Fore.RESET}\n'
                f'Требования: {Fore.LIGHTYELLOW_EX}{self.requirement}{Fore.RESET}\n')

    def __gt__(self, other):
        """
        Сравнение зарплаты
        :param other: зарплата другой вакансии
        :return: вакансию с большей зарплатой
        """
        if self.salary_vacs is not None and other.salary_vacs is not None:
            if self.salary_vacs["from"] > other.salary_vacs["from"]:
                return self
            else:
                return other
        return "Зарплата не указана"

    def __lt__(self, other):
        """
        Сравнение зарплаты
        :param other: зарплата другой вакансии
        :return: вакансию с меньшей зарплатой
        """
        if self.salary_vacs is not None and other.salary_vacs is not None:
            if self.salary_vacs["from"] < other.salary_vacs["from"]:
                return self
            else:
                return other
        return "Зарплата не указана"

    @property
    def name(self):
        if self.name_vacs is not None:
            return self.name_vacs

    @property
    def url(self):
        if self.url_vacs is not None:
            return self.url_vacs
        else:
            return "Ссылка вакансии не указана"

    @property
    def city(self):
        if self.city_vacs is not None:
            self.city_vacs = self.city_vacs
            return self.city_vacs
        else:
            return "Город вакансии не указан"

    @property
    def desc(self):
        if self.desc_vacs is not None:
            return self.desc_vacs
        else:
            return "Описание вакансии не указано"

    @property
    def salary(self):
        """
        Проверка зарплаты вакансии
        :return: Размер, если зарплата указана и "Зарплата не указана" если не указана
        """
        if self.salary_vacs is None:
            self.salary_vacs = "Зарплата не указана"
            return self.salary_vacs
        if self.salary_vacs['to'] is None:
            return f"От {self.salary_vacs['from']} {self.salary_vacs['currency']}"
        if self.salary_vacs['from'] is None:
            return f"До {self.salary_vacs['to']} {self.salary_vacs['currency']}"
        else:
            return f"От {self.salary_vacs['from']} до {self.salary_vacs['to']} {self.salary_vacs['currency']}"

    @property
    def requirement(self):
        if self.requirement_vacs is not None:
            self.requirement_vacs = self.requirement_vacs
            return self.requirement_vacs
        else:
            return "Не описаны требования вакансии"

    @staticmethod
    def create_list_obj(list_obj):
        """
        Создание списка экз класса Vacancy
        :param list_obj: данные для создания экз класса
        :return: list_vacancies: список экз класса
        """
        list_vacancies = []
        for i in list_obj['items']:
            list_vacancies.append(
                Vacancy(i['name'],
                        i['alternate_url'],
                        i['area']['name'],
                        i['snippet']['responsibility'],
                        i['salary'],
                        i['snippet']['requirement']))
        return list_vacancies
