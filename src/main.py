import src.functions


def five_transactions(json_path):
    """ Возвращает 5 крайних успешных транзакций. """
    five_transaction = []
    for el in range(5):
        five_transaction.append(
            src.functions.get_sort_transactions(json_path)[el])
    return five_transaction
