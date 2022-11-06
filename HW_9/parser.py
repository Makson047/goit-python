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
    elif not correct_phone(phone_number):
        raise ValueError('Bad input phone number!')
    else:
        return 'add', [user_name, phone_number]


def change_parser(user_command: str):
    args = user_command.lstrip('change ')
    user_name, phone_number = args.strip().split(' ')
    if user_name == '':
        raise ValueError('Bad input name!')
    elif not correct_phone(phone_number):
        raise ValueError('Bad input phone number!')
    else:
        return 'change', [user_name, phone_number]


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
    "good bye": close_parser,
    "close": close_parser,
    "exit": close_parser
}


def correct_phone(phone):
    if len(phone) < 10 or len(phone) > 17:
        print('Phone must be 10-17 characters without letters')
        return False
    for i in phone[0]:
        if i in ascii_letters:
            print('Phone must be 10-17 characters without letters')
            return False

    return True


@parser_handler
def user_command_parser(user_command: str) -> tuple[str, list]:
    for command in command_parser.keys():
        normalized_input = ' '.join(list(filter(lambda x: x != '', user_command.lower().split(' '))))
        normalized_input = normalized_input.ljust(len(normalized_input) + 1, ' ')
        if normalized_input.startswith(command + ' '):
            parser = command_parser.get(command)
            return parser(user_command=normalized_input)
    raise ValueError('Unknown command! Please enter another command')