from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value: str):
        self.__value = None
        self.value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if not all((value.startswith('+'), len(value) == 13, value[1:].isdigit())):
            raise ValueError("Please, enter the phone number in format: '+380111111111'")
        self.__value = value


class Birthday(Field):
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        return datetime.strftime(self.__value, '%d.%m.%Y')

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        try:
            date_birthday = datetime.strptime(value, '%d.%m.%Y')
            self.__value = date_birthday
        except:
            raise ValueError("Please, enter the birthday date in format: 'dd.mm.yyyy' (example 01.01.1990)")


class AddressBook(UserDict):

    def add_contact(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        contact = Record(name=name, phone=phone, birthday=birthday)
        self.data[name.value] = contact

    def add_record(self, record: 'Record'):
        self.data[record.name.value] = record

    def iterator(self, page_number, num_of_records):
        new_data = list(self.data.items())
        total_items = page_number * num_of_records
        yield list(new_data[(total_items - num_of_records):total_items])


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []
        self.birthday = birthday

    def __repr__(self):
        return f'{self.name.value}: {" ".join(phone.value for phone in self.phones)}'

    def add_phone(self, phone_number: Phone):
        self.phones.append(phone_number)

    def change_phone(self, old_number: Phone, new_number: Phone):
        try:
            self.delete_phone(old_number)
            self.add_phone(new_number)
        except ValueError:
            return f'{old_number} does not exist'

    def delete_phone(self, old_phone: Phone):
        for phone in self.phones:
            try:
                if phone.value == old_phone:
                    self.phones.remove(phone)
            except ValueError:
                print(f"\nPhone number: {phone} doesn't exist")

    def add_birthday(self, birthday : Birthday):
        self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now().date()
            if self.birthday.value.replace(year=today.year) >= today:
                result = (self.birthday.value.replace(year=today.year) - today).days
            else:
                result = (self.birthday.value.replace(year=today.year + 1) - today).days
            return result
        else:
            return "If you want to know which days left to contact's birthday, then use command: 'set birthday' "