from typing import Dict, Callable
from contacts import contacts_book


def command_handler(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception:
            raise SystemExit('Good bye!')

    return wrapper


@command_handler
def hello_handler(*args):
    return 'How can I help you?'


@command_handler
def add_handler(user_name: str, phone_number: str):
    if contacts_book.get(user_name) is None:
        contacts_book[user_name] = phone_number
        return 'Contact was added'
    raise ValueError('Contact already exists!')


@command_handler
def change_handler(user_name: str, phone_number: str):
    if contacts_book.get(user_name) is not None:
        contacts_book[user_name] = phone_number
        return 'Contact was changed'
    raise KeyError('Contact does not exists!')


@command_handler
def phone_handler(user_name: str):
    phone_number = contacts_book.get(user_name)
    if phone_number is not None:
        return f'{user_name} number is: {phone_number}'
    raise ValueError('')


@command_handler
def show_all_handler(*args):
    contacts = '\n'.join(
        f'{user_name} number is: {phone_number}' for (user_name, phone_number) in contacts_book.items()
    )
    contacts_response = 'Contacts does not exists yet!' if contacts == '' else contacts
    return 'Contacts book: \n' + contacts_response


@command_handler
def close_handler(*args):
    raise SystemExit('Good bye!')


@command_handler
def error_command_handler(*args):
    raise ValueError('Command is wrong!')


handlers: Dict[str, Callable] = {
    "hello": hello_handler,
    "add": add_handler,
    "change": change_handler,
    "phone": phone_handler,
    "show all": show_all_handler,
    "good bye": close_handler,
    "close": close_handler,
    "exit": close_handler
}