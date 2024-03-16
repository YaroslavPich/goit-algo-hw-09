from classes import AddressBook, Record
from view import ConsoleAddressBookView
import pickle


def input_error(func):
    """Error handling."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter correct data."
        except IndexError:
            return "Enter correct data."
        except TypeError:
            return "Enter correct data."

    return inner


class AddressBookController:
    def __init__(self):
        self.book = AddressBook()
        self.view = ConsoleAddressBookView()

    @input_error
    def add_birthday(self, args):
        """Adding a birthday."""
        name, birthday = args
        record = self.book.find(name)
        if not record:
            record = Record(name)
            self.book.add_record(record)
        record.add_birthday(birthday)
        return f"Birthday {name} - {birthday} added."

    @input_error
    def add_contact(self, args):
        """Adding a contact."""
        name, phone = args
        record = self.book.find(name)
        if not record:
            record = Record(name)
            self.book.add_record(record)
        record.add_phone(phone)
        return f"Contact {name} with phone - {phone} added."

    @input_error
    def birthdays(self):
        """Bringing birthdays forward by 7 days."""
        birthdays = self.book.get_upcoming_birthdays()
        return birthdays

    @input_error
    def change_contact(self, args) -> str:
        """Overwriting a contact"""
        name, old_phone, new_phone = args
        record = self.book.find(name)
        if not record:
            return f"{name} not found."
        else:
            record.edit_phone(old_phone, new_phone)
            return f"Contact {name} changed his old number {old_phone}\
                  to {new_phone} new number."

    def load_data(self, filename="addressbook.pkl"):
        """Downloading from a file."""
        try:
            with open(filename, "rb") as f:
                self.book = pickle.load(f)
        except FileNotFoundError:
            self.book = AddressBook()

    def parse_input(self, user_input: str) -> tuple:
        """Command recognition"""
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    def save_data(self, filename="addressbook.pkl"):
        """Writing to a file."""
        with open(filename, "wb") as f:
            pickle.dump(self.book, f)

    def show_all(self) -> str:
        """Output of all contacts!"""
        if self.book:
            return self.book.data
        else:
            return "There is no contact!"

    @input_error
    def show_birthday(self, args):
        """Date of birth by contact."""
        name = args[0]
        record = self.book.find(name)
        if not record:
            return f"Contact {name} not found."
        else:
            return record.birthday

    @input_error
    def show_phone(self, args) -> str:
        """Contact output by given name."""
        name = args[0]
        record = self.book.find(name)
        if not record:
            return f"Contact {name} not found."
        else:
            return ", ".join(str(phone) for phone in record.phones)

    @input_error
    def command(self, user_input):
        """'The main program."""
        command, *args = self.parse_input(user_input)

        if command in ("close", "exit"):
            self.view.display_message("Good bye!")
            return False
        elif command == "hello":
            self.view.display_message("How can I help you?")
        elif command == "add":
            self.view.display_message(self.add_contact(args))
        elif command == "change":
            self.view.display_message(self.change_contact(args))
        elif command == "phone":
            self.view.display_message(self.show_phone(args))
        elif command == "all":
            self.view.display_contacts_table(self.show_all())
        elif command == "add-birthday":
            self.view.display_message(self.add_birthday(args))
        elif command == "show-birthday":
            self.view.display_message(self.show_birthday(args))
        elif command == "birthdays":
            self.view.display_contacts_birthdays(self.birthdays())
        elif command == "command":
            self.view.display_command_list()
        else:
            self.view.display_message("Invalid command.")
        return True
