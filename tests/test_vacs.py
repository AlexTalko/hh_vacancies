import pytest
from src.vacs import Vacancy


@pytest.fixture
def vacs():
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
                    {'from': None, 'to': 20000, 'currency': 'рублей'},
                    None
                    )
    vacs3 = Vacancy('Курьер',
                    'https://www.hh.ru/vacancy/123456',
                    'Казань',
                    'Курьер на личный ТС',
                    None,
                    'Знание города'
                    )
    return vacs1, vacs2, vacs3


def test_vacancy(vacs):
    vacs1, vacs2, vacs3 = vacs
    assert vacs1.name == 'Водитель'
    assert vacs1.url == 'https://www.hh.ru/vacancy/12345'
    assert vacs1.city == 'Москва'
    assert vacs1.desc == 'Водитель самосвала'
    assert vacs2.desc == 'Описание вакансии не указано'
    assert vacs1.salary == 'От 1000 до 10000 RUR'
    assert vacs2.salary == 'До 20000 рублей'
    assert vacs3.salary == 'Зарплата не указана'
    assert vacs2.requirement == 'Не описаны требования вакансии'

