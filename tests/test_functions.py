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
