from colorama import *


def sort_salary_from(vacs_list, user_option_sort):
    """
    Функция для списка вакансий по зарплате
    :param vacs_list: список вакансий
    :param user_option_sort: опция сортировки
    :return: отсортированный список
    """
    if user_option_sort == 1:
        vacs_list.sort(key=lambda x: x.salary)
        print(Fore.LIGHTBLUE_EX + 'Сортировка по возрастанию зарплаты')
        if user_option_sort == 2:
            vacs_list.sort(key=lambda x: x.salary, reverse=True)
            print(Fore.LIGHTBLUE_EX + 'Сортировка по убыванию зарплаты')
            if user_option_sort == 3:
                print(Fore.LIGHTRED_EX + 'Без сортировки списка вакансий')
                return vacs_list
