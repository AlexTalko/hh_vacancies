import pytest
from src.func import sort_salary_from
from src.vacs import Vacancy


@pytest.fixture
def vacs():
    vacs_list = []
    vacs1 = Vacancy('Водитель',
                    'https://www.hh.ru/vacancy/12345',
                    'Москва',
                    'Водитель самосвала',
                    {'from': 1000, 'to': 10000, 'currency': 'RUR'},
                    'права категории D'
                    )
    vacs2 = Vacancy('Няня',
                    'https://www.hh.ru/vacancy/1234567',
                    'Саранск',
                    None,
                    {'from': None, 'to': 10000, 'currency': 'RUR'},
                    None
                    )
    vacs3 = Vacancy('Курьер',
                    'https://www.hh.ru/vacancy/123456',
                    'Казань',
                    'Курьер на личный ТС',
                    {'from': 80000, 'to': 90000, 'currency': 'RUR'},
                    'Знание города'
                    )
    vacs_list.append(vacs1)
    vacs_list.append(vacs2)
    vacs_list.append(vacs3)
    return vacs_list


def test_sort_salary_from(vacs):
    vacs_list = vacs
    sort_salary_from(vacs_list, 1)  # тест сортировки по возрастанию
    assert vacs_list[0].salary == 'До 10000 RUR'
    assert vacs_list[1].salary == 'От 1000 до 10000 RUR'
    assert vacs_list[2].salary == 'От 80000 до 90000 RUR'
    sort_salary_from(vacs_list, 2)  # тест сортировки по убыванию
    assert vacs_list[0].salary == 'От 80000 до 90000 RUR'
    assert vacs_list[1].salary == 'От 1000 до 10000 RUR'
    assert isinstance(vacs_list, list) is True
