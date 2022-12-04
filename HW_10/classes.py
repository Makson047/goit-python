from collections import UserDict


class Field:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class AddressBook(UserDict):

    def add_contact(self, name: Name, phone: Phone = None):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record: 'Record'):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []

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

    def delete_phone(self, phone: Phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f'{phone} does not exist'
