import src.functions


def five_transactions(json_path):
    """ Возвращает 5 крайних успешных транзакций. """
    five_transaction = []
    for el in range(5):
        five_transaction.append(
            src.functions.get_sort_transactions(json_path)[el])
    return five_transaction


def get_transaction(json_path):
    """ Возвращает список 5 крайних успешных транзакций в заданном формате. """
    info_str = ''
    for el in five_transactions(json_path):
        info_str_1 = (f'{src.functions.date_show(el.get('date'))} '
                      f'{el.get('description')}\n')

        if src.functions.format_from_account(el.get('from')) is None:
            info_str_2 = f'{src.functions.format_to_account(el.get('to'))}\n'
        else:
            info_str_2 = (
                f'{src.functions.format_from_account(el.get('from'))} '
                f'-> {src.functions.format_to_account(el.get('to'))}\n')

        info_str_3 = (f'{el.get('operationAmount').get('amount')} '
                      f'{el.get('operationAmount').get('currency').get('name')}\n')

        info_str += info_str_1
        info_str += info_str_2
        info_str += info_str_3 + '\n'

    return info_str


if __name__ == '__main__':
    print(get_transaction('operations.json'))
