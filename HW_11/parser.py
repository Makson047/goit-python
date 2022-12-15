from handler import handlers
from string import ascii_letters


def parser_handler(func):
    def wrapper(user_command: str):
        try:
            return func(user_command)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)

    return wrapper


def hello_parser(user_command: str):
    return 'hello', []


def add_parser(user_command: str):
    args = user_command.lstrip('add ')
    user_name, phone_number = args.strip().split(' ')
    if user_name == '':
        raise ValueError('Bad input name!')
    else:
        return 'add', [user_name, phone_number]


def change_parser(user_command: str):
    args = user_command.lstrip('change ')
    user_name, new_phone_number = args.strip().split(' ')
    if user_name == '':
        raise ValueError('Bad input name!')
    else:
        return 'change', [user_name, new_phone_number]


def phone_parser(user_command: str):
    user_name = user_command.strip().lstrip('phone ')
    if user_name == '':
        raise ValueError('Bad input name!')
    else:
        return 'phone', [user_name]


def show_all_parser(user_command: str):
    if user_command == 'show all ':
        return 'show all', []
    else:
        raise ValueError('Bad input!')


def set_birthday_parser(user_command: str):
    args = user_command.lstrip('set birthday ')
    user_name, birthday = args.strip().split(' ')
    if user_name == '':
        raise ValueError('Bad input name!')
    else:
        return 'set birthday', [user_name, birthday]


def show_birthday_parser(user_command: str):
    user_name = user_command.strip().lstrip('show birthday ')
    if user_name == '':
        raise ValueError('Bad input name!')
    else:
        return 'show birthday', [user_name]


def close_parser(user_command: str):
    for item in ['good bye ', 'close ', 'exit ']:
        if item == user_command:
            return 'close', []
    raise ValueError('Bad input!')


command_parser = {
    "hello": hello_parser,
    "add": add_parser,
    "change": change_parser,
    "phone": phone_parser,
    "show all": show_all_parser,
    "set birthday": set_birthday_parser,
    "show birthday": show_birthday_parser,
    "good bye": close_parser,
    "close": close_parser,
    "exit": close_parser
}


@parser_handler
def user_command_parser(user_command: str) -> tuple[str, list]:
    for command in command_parser.keys():
        normalized_input = ' '.join(list(filter(lambda x: x != '', user_command.split(' '))))
        normalized_input = normalized_input.ljust(len(normalized_input) + 1, ' ')
        if normalized_input.startswith(command + ' '):
            parser = command_parser.get(command)
            return parser(user_command=normalized_input)
    raise ValueError('Unknown command! Please enter another command')