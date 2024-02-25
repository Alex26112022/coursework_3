from config import operations_path
from src.main import *


def test_five_transactions():
    """ Проверка количества возвращаемых транзакций. """
    assert len(five_transactions(operations_path)) == 5


def test_get_transaction():
    """ Тестирует итоговую функцию. """
    assert get_transaction(operations_path) == (
        '08.12.2019 Открытие вклада\n'
        'Счет **5907\n'
        '41096.24 USD\n'
        '\n'
        '07.12.2019 Перевод организации\n'
        'Visa Classic 2842 87** **** 9012 -> Счет **3655\n'
        '48150.39 USD\n'
        '\n'
        '19.11.2019 Перевод организации\n'
        'Maestro 7810 84** **** 5568 -> Счет **2869\n'
        '30153.72 руб.\n'
        '\n'
        '13.11.2019 Перевод со счета на счет\n'
        'Счет 3861 14** **** 9794 -> Счет **8125\n'
        '62814.53 руб.\n'
        '\n'
        '05.11.2019 Открытие вклада\n'
        'Счет **8381\n'
        '21344.35 руб.\n'
        '\n')
