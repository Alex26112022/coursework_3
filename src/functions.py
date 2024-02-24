import json
from datetime import datetime


def load_json(json_file) -> list:
    """ Считывает json данные по транзакциям и возвращает список словарей. """
    with open(json_file, 'r', encoding='utf-8') as f:
        file = f.read()
        file = json.loads(file)
    return file
