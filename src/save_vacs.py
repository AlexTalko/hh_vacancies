import json
import os
import requests
from abc import ABC, abstractmethod
from colorama import *


class API(ABC):
    """
    API base class.
    """

    @abstractmethod
    def get_vacs(self, query):
        pass


class HeadHunter(API):
    """
    Класс для подключения к API hh.ru и получения вакансий
    по ключевому слову
    """

    def get_vacs(self, query=None):
        """
        Получение вакансий по ключевому слову с ресурса 'https://api.hh.ru/vacancies'
        :param query: ключевое слово
        :return: вакансии по ключевому слову
        """
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, params={'text': query, 'per_page': 100, 'area': '113'})  # 'area': '113' - Россия
        return response.json()


class Saver(ABC):

    @abstractmethod
    def create_file(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_file(self, *args, **kwargs):
        raise NotImplementedError


class JSONSaver(Saver):
    """
    Класс для сохранения вакансий в файл
    """

    def __init__(self, file_save):
        """
        Конструктор класса JSONSaver
        :param file_save: имя файла для сохранения вакансий
        """
        self.file_save = file_save

    def create_file(self, data) -> None:
        """
        Создание файла для сохранения вакансий
        :param data: данные для сохранения
        """
        os.chdir('data/')
        with open(self.file_save, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(Fore.GREEN + 'Информация о вакансиях сохранена в файл vacancies.json' + Fore.RESET)

    def delete_file(self, file_del) -> None:
        """
        Удаление файла вакансий
        """
        os.remove(file_del)
        print(Fore.GREEN + f'Файл {file_del} удален' + Fore.RESET)
