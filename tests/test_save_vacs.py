import pytest
from src.save_vacs import HeadHunter, JSONSaver


@pytest.fixture
def hh():
    """Функция для создания объекта HeadHunter"""
    hh = HeadHunter()
    vacancies = hh.get_vacs()
    return hh, vacancies


def test_hh(hh):
    hh, vacancies = hh
    assert isinstance(hh, HeadHunter)
    assert isinstance(vacancies['items'], list)
    assert len(vacancies['items']) > 1
    assert isinstance(vacancies['items'][0], dict)
