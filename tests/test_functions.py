import pytest
from src.functions import *
from datetime import datetime


def test_load_json():
    """ Проверка соответствия типа загружаемых данных. """
    assert type(load_json('operations.json')) == list
    assert type(load_json('operations.json')[0]) == dict


def test_date_format():
    new_date = datetime(2024, 2, 22, 10, 30, 20, 294041)
    """ Проверка перевода даты из str в datetime. """
    assert date_format("2024-02-22T10:30:20.294041") == new_date


@pytest.mark.parametrize('date_str, date_obj',
                         [('2019-07-03T18:35:29.512364', '03.07.2019'),
                          ('2019-04-04T23:20:05.206878', '04.04.2019'),
                          ('2018-02-22T00:40:19.984219', '22.02.2018'),
                          ('2018-06-04T06:59:55.424356', '04.06.2018')])
def test_date_show(date_str, date_obj):
    """ Проверка форматирования отображаемой даты. """
    assert date_show(date_str) == date_obj
