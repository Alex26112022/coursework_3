from src.main import *


def test_five_transactions():
    """ Проверка количества возвращаемых транзакций. """
    assert len(five_transactions('operations.json')) == 5
