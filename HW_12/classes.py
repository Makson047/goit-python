from collections import UserDict
from datetime import datetime
import pickle
import copy


class Field:
    def __init__(self, value: str):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value: str):
        if not all((value.startswith('+'), len(value) == 13, value[1:].isdigit())):
            raise ValueError("Please, enter the phone number in format: '+380111111111'")
        self.__value = value


class Birthday(Field):
    @Field.value.setter
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
        new_data = list()
        names = sorted([name for name in self.data])
        for name in names:
            contact = ''
            record = self.data[name]
            contact += f'Name: {record.name.value}; Phone: '
            for phone in record.phones:
                contact += f'{phone} '
            contact += f'; Birthday: {str(record.birthday)}'
            new_data.append(contact)
        total_items = page_number * num_of_records
        yield list(new_data[(total_items - num_of_records):total_items])

    def find_contact(self, text):
        lst_records = []
        for name, data in self.data.items():
            if name.lower().find(text.lower()) != -1:
                lst_records.append(self.data[name])
            else:
                for phone in data.phones:
                    if phone.value.find(text) != -1:
                        lst_records.append(
                            Record(data.name.value, phone.value, data.birthday.value))
                        break
        if lst_records:
            for record in lst_records:
                text_records = ''
                try:
                    record_name = record.name.value
                except:
                    record_name = record.name
                record_birthday = str(record.birthday)
                for phone in record.phones:
                    try:
                        text_records += '{:<20}{:>20}{:>20}'.format(record_name, phone.value, record_birthday)
                    except:
                        text_records += '{:<20}{:>20}{:>20}'.format(record_name, phone, record_birthday)
                    record_name = ''
                    record_birthday = ''
                if record_name:
                    text_records += '{:<20}{:>20}{:>20}'.format(record_name, '', record_birthday)

                yield text_records
        else:
            yield "Records don't found!"

    def save_to_file(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, "rb") as file:
            content = pickle.load(file)
        return content


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name: Name = name
        self.phones: list[Phone] = [phone] if phone is not None else []
        self.birthday = birthday

    # def __repr__(self):
    #     return f'{self.name.value}: {" ".join(phone.value for phone in self.phones)}'

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
            today = datetime.now()
            bday = datetime.strptime(self.birthday.value, '%d.%m.%Y').replace(year=today.year)
            if bday > today:
                result = (bday - today).days
            else:
                result = (bday.replace(year=today.year + 1) - today).days
            return result
        else:
            return "If you want to know which days left to contact's birthday, then use command: 'set birthday' "