import config

_BALANCE = 'Ваш депозит: {} ETH. \n\n' \
           'Ваш баланс: {} ETH. \n\n' \
           'Процентная ставка: {}% в день.\n\n' \
           'После пополнения счета, сумма на счете будет расти' \
           ' в соответствии с установленной процентной ставкой, а также количеством Ваших рефералов.\n\n' \
           'Для начисления процентов сумма депозита должна быть не менее {} ETH'

_TOP_UP = 'ETH адрес для инвестиций: {}\n\n' \
          'Вы можете переводить на этот адрес любую сумму в любое время с вашего привязанного кошелька. ' \
          'Средства будут зачислены на Ваш счет в течение часа. Успешных инвестиций!'

_WALLET_NOT_SET = 'Ваш адрес для вывода не установлен\n'

_WITHDRAW = 'Ваш адрес для вывода: {}.\n' \
            'Средства будут перечислены на указанный Вами адрес в ближайшее время (обычно в течение часа).\n' \
            'Чтобы изменить адрес ETH кошелька для вывода, введите /wallet <ваш кошелёк>.\n' \
            'Для вывода монет введите /withdraw <сумма>.'

_WALLET_SET = 'ETH кошелёк {} успешно привязанн к вашему аккаунту.'

_ENTER_NEW_WALLET = 'Введите новый адрес для вывода:'

_WITHDRAWN = 'Ваши средства успешно поставлены на вывод на кошелек {} и ждут подтвержения.'

_WITHDRAW_HOW_MUCH = 'Сколько вы хотите вывести?'

_INVALID_INPUT = 'Введите валидное значение.'

_WALLET_IS_TAKEN = 'Данный eth адрес уже занят.'

_PARTNERS = 'Ваша реферальная ссылка: {}\n'

_BACK_TO_MAIN_MENU = 'Возврат в главное меню.'

_TOP_UPS = 'Ваши пополнения:\n'

_NO_TOP_UPS = 'У вас пока нет пополнений.'

_WITHDRAWALS = 'Ваши выводы:\n'

_NO_WITHDRAWALS = 'У вас пока нет выводов.'

_NOT_REGISTERED = 'Вы не зарегистрированны в системе. Для начала введите команду /start.'


def eth_address_taken():
    return _WALLET_IS_TAKEN


def not_registered():
    return _NOT_REGISTERED


def withdrawals(withdrawals_list):
    if len(withdrawals_list) == 0:
        return _NO_WITHDRAWALS
    withdrawals = _WITHDRAWALS
    for withdrawal, index in withdrawals_list:
        withdrawals += index + '. ' + withdrawal + '\n'
    return withdrawals


def top_ups(top_ups_list):
    if len(top_ups_list) == 0:
        return _NO_TOP_UPS
    top_ups = _TOP_UPS
    for top_up, index in top_ups_list:
        top_ups += index + '. ' + top_up + '\n'
    return top_ups


def back_to_main_menu():
    return _BACK_TO_MAIN_MENU


def partners(user_id, user_invited_by=None):
    partners_info = ''
    if user_invited_by:
        partners_info = 'Вы были приглашены пользователем: @{}\n'.format(user_invited_by.username)
    partners_info += _PARTNERS
    referral_link = 'https://telegram.me/' + config.get_bot_username() + '?start=' + str(user_id)
    return partners_info.format(referral_link)


def invalid_input():
    return _INVALID_INPUT


def wallet_successfully_set(wallet):
    return _WALLET_SET.format(wallet)


def deposit(user_deposit, user_balance, percent, minimal_deposit):
    return _BALANCE.format(user_deposit, user_balance, percent, minimal_deposit)


def top_up():
    return _TOP_UP.format(config.get_eth_address())


def withdraw(wallet):
    return _WITHDRAW.format(wallet)


def wallet_not_set():
    return _WALLET_NOT_SET


def enter_new_wallet():
    return _ENTER_NEW_WALLET


def withdrawn(wallet):
    return _WITHDRAWN.format(wallet)


def withdraw_how_much():
    return _WITHDRAW_HOW_MUCH