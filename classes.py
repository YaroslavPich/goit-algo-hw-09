from collections import UserDict
from datetime import datetime, timedelta


class Field:
    """Base class for record fields."""

    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """Class for storing a contact name."""

    def __init__(self, value: str):
        if not value:
            raise ValueError
        else:
            super().__init__(value)


class Phone(Field):
    """Class for storing a phone number."""

    def __init__(self, value: str):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError


class Birthday(Field):
    """Creating a birthday class"""

    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError


class Record:
    """Class for storing information about a contact, including name and phone
    list."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def find_phone(self, phone: str):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None

    def remove_phone(self, phone: str) -> bool:
        ph = self.find_phone(phone)
        if ph:
            self.phones.remove(ph)
            return True
        else:
            return False

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
            return True
        else:
            raise ValueError

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value.capitalize()}\
            , phones: {'; '.join(p.value for p in self.phones)},\
                  Birthday: {self.birthday}"


class AddressBook(UserDict):
    """Class for storing and managing records."""

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        else:
            return False

    def get_upcoming_birthdays(self: Record) -> list:
        today = datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
                birthday_date = datetime.strptime(
                    record.birthday.value, "%d.%m.%Y"
                ).date()
                birthday_this_year = birthday_date.replace(year=today.year)
                if today <= birthday_this_year <= today + timedelta(days=7):
                    if birthday_this_year.isoweekday() == 6:
                        birthday_this_year += timedelta(days=2)
                    elif birthday_this_year.isoweekday() == 7:
                        birthday_this_year += timedelta(days=1)
                    congratulation_date_str \
                        = birthday_this_year.strftime("%Y.%m.%d")
                    upcoming_birthdays.append((name, congratulation_date_str))
        return upcoming_birthdays

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


if __name__ == "__main__":
    book = AddressBook()
