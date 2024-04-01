from src.func import sort_salary_from
from src.save_vacs import HeadHunter, JSONSaver
from src.vacs import Vacancy
from colorama import *


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    print(Fore.LIGHTBLUE_EX + 'Добро пожаловать в мини версию HH.ru!')
    user_query = str(input('Какую вакансию хотите найти?\n'
                           'Нажмите Enter, или введите любое число для поиска случайных вакансий\n').lower())

    # подключаемся к API hh.ru
    hh = HeadHunter()

    # получаем вакансии с hh.ru по ключевому слову
    vacancies = hh.get_vacs(user_query)

    # сохраняем вакансии в файл vacancies.json
    file = JSONSaver('vacancies.json')
    file.create_file(vacancies)

    # создаем список объектов Vacancy
    vacs_list = Vacancy.create_list_obj(vacancies)

    # сортируем список вакансий по зарплате
    user_option_sort = int(input(Fore.LIGHTYELLOW_EX + 'Наберите номер для сортировки списка вакансий:\n'
                                                       '1 - сортировка по возрастанию зарплаты\n'
                                                       '2 - сортировка по убыванию зарплаты\n'
                                                       '3 - без сортировки\n'
                                                       '*сортировка работает без учета курса валют\n'))
    sort_salary_from(vacs_list, user_option_sort)

    # запрашиваем N количество для вывода вакансий
    n = int(input(Fore.GREEN + 'Введите количество вакансий для вывода: '))

    # выводим N вакансий
    for i in range(n):
        print(Fore.LIGHTBLUE_EX + f'{vacs_list[i]}')

    # запрашиваем удаление файла вакансий
    delete_file = input(Fore.LIGHTBLUE_EX + 'Удалить файл вакансий(y/n)?')
    if delete_file in ['y', 'yes', 'да']:
        file.delete_file('vacancies.json')

    # запрашиваем у пользователя закончить работу или начать заново
    user_option = input(Fore.LIGHTBLUE_EX + 'Начать поиск заново?(y/n)?')
    if user_option in ['y', 'yes', 'да']:
        print(Fore.LIGHTMAGENTA_EX + '***MAGIC MOMENT***')
        user_interaction()
    else:
        print(Fore.LIGHTYELLOW_EX + 'Программа завершена. Удачи!')
        exit()


if __name__ == "__main__":
    user_interaction()
