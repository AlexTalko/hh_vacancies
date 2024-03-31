import json
import os
import requests
from abc import ABC, abstractmethod


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
        response = requests.get(url, params={'text': query, 'per_page': 100})
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
        self.file_save = file_save

    def create_file(self, data) -> None:
        """
        Создание файла для сохранения вакансий
        :param data: данные для сохранения
        """
        os.chdir('../data/')
        with open(self.file_save, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def delete_file(self) -> None:
        """
        Удаление файла вакансий
        """
        os.chdir('../data/')
        try:
            os.remove(self.file_save)
        except FileNotFoundError:
            pass
