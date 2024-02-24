import json
from datetime import datetime


def load_json(json_file) -> list:
    """ Считывает json данные по транзакциям и возвращает список словарей. """
    with open(json_file, 'r', encoding='utf-8') as f:
        file = f.read()
        file = json.loads(file)
    return file


def date_format(date_str: str) -> datetime:
    """ Принимает дату в строковом формате и возвращает в формате даты."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date_obj


def date_show(date_str: str) -> str:
    """ Принимает дату в строковом формате и возвращает строку в формате
    '%d.%m.%Y'. """
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    str_date = datetime.strftime(date_obj, '%d.%m.%Y')
    return str_date
