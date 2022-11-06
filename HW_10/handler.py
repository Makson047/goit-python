from typing import Dict, Callable
from classes import *

dict_phones = AddressBook()


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
    name = Name(user_name.lower())
    phone = Phone(phone_number)

    if name in dict_phones:
        record = dict_phones.data[name]
        record.add_phone(phone)
    else:
        record = Record(name=name, phone=phone)
        dict_phones.add_record(record)

    return f'Contact {name}: {phone} was created!'


@command_handler
def change_handler(user_name: str, phone_number: str):
    name = Name(user_name)
    phone = Phone(phone_number)

    if name.value in dict_phones:
        record = dict_phones.data[name.value]
        record.change_phone(record.phones[0], phone)
        return f'For contact {name} phone number was changed to {phone}'
    raise KeyError('Contact does not exists!')


@command_handler
def phone_handler(user_name: str):
    name = Name(user_name)
    record = dict_phones.data[name.value]
    return ', '.join([phone.value for phone in record.phones])


@command_handler
def show_all_handler(*args):

    contacts = ''
    for name, record in dict_phones.items():
        contacts += '\n' + name + ' number is: ' + ', '.join([phone.value for phone in record.phones])
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