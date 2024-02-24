import pytest
from src.functions import load_json
from datetime import datetime


def test_load_json():
    """ Проверка соответствия типа загружаемых данных. """
    assert type(load_json('operations.json')) == list
    assert type(load_json('operations.json')[0]) == dict
