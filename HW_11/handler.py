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
            raise SystemExit('Something is wrong, goodbye!')

    return wrapper


@command_handler
def hello_handler(*args):
    return 'How can I help you?'


@command_handler
def add_handler(user_name: str, phone_number: str):
    name = Name(user_name)
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
    new_phone = Phone(phone_number)

    if name.value in dict_phones:
        old_phone = input('Enter phone number to change: ')
        record = dict_phones.data[name.value]
        record.change_phone(old_phone, new_phone)
        return f'For contact {name} phone number was changed from {old_phone} to {new_phone}'
    raise KeyError('Contact does not exists!')


@command_handler
def phone_handler(user_name: str):
    name = Name(user_name)
    record = dict_phones.data[name.value]
    return ', '.join([phone.value for phone in record.phones])


@command_handler
def show_all_handler(*args):
    page_number = int(input('Enter page number: '))
    num_of_records = int(input('How many records we need: '))
    page = dict_phones.iterator(page_number, num_of_records)
    return 'Contacts book: \n' + f'{next(page)}'


@command_handler
def set_birthday_handler(user_name: str, birthday: str):
    name = Name(user_name)
    bday = Birthday(birthday)
    if name.value in dict_phones:
        record = dict_phones.data[name.value]
        record.add_birthday(bday)
        print(f'Birthday: {bday.value} has added to {name.value}')
    else:
        print(f"Contact '{name.value}' doesn't exist")


@command_handler
def show_birthday_handler(user_name: str):
    name = Name(user_name)
    if name.value in dict_phones:
        days = dict_phones.data[name.value].days_to_birthday()
        print(f"To Birthday left: {days} days")
    else:
        print(f"Contact '{name.value}' doesn't exist or birthday doesn't enter")


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
    "set birthday": set_birthday_handler,
    "show birthday": show_birthday_handler,
    "good bye": close_handler,
    "close": close_handler,
    "exit": close_handler
}