from abc import ABC, abstractmethod


class AddressBookView(ABC):
    @abstractmethod
    def display_message(self, message):
        pass

    @abstractmethod
    def display_contacts_table(self, contacts):
        pass

    @abstractmethod
    def display_contacts_rows(self, contacts):
        pass

    @abstractmethod
    def display_contacts_birthdays(self, birthdays):
        pass

    @abstractmethod
    def display_command_list(self):
        pass


class ConsoleAddressBookView(AddressBookView):
    def display_message(self, message):
        print(message)

    def display_contacts_table(self, contacts):
        if contacts:
            print("{:^20}|{:^20}|{:^20}".format("Name", "Phones", "Birthday"))
            print("-" * 60)
            for contact in contacts.values():
                name = contact.name.value.capitalize()
                phones = "; ".join(str(phone) for phone in contact.phones)
                birthday = contact.birthday.value if contact.birthday else ""
                print("{:^20}|{:^20}|{:^20}".format(name, phones, birthday))
        else:
            print("No contacts!")

    def display_contacts_rows(self, contacts):
        if contacts:
            for contact in contacts.values():
                name = contact.name.value.capitalize()
                phones = "; ".join(str(phone) for phone in contact.phones)
                birthday = contact.birthday.value if contact.birthday else ""
                print(
                    f"Contact {name}",
                    f"has number {phones}" if phones else "no number",
                    f"birthday {birthday}" if birthday else "no information",
                )

    def display_contacts_birthdays(self, birthdays):
        if birthdays:
            print("{:^20}|{:^20}".format("Name", "Birthday"))
            print("-" * 40)
            for name, birthday in birthdays:
                print("{:^20}|{:^20}".format(name, birthday))
        else:
            print("No upcoming birthdays!")

    def display_command_list(self):
        print("{:^20}|{:^50}".format("Command", "Description"))
        print("-" * 70)
        commands = [
            (" add", " Add a new contact"),
            (" change", " Change contact"),
            (" phone", " Show the contact's phone number"),
            (" all", " Show all contacts"),
            (" add-birthday", " Add birthday"),
            (" show-birthday", " Show a contact's birthday"),
            (" birthdays", " Show upcoming birthdays"),
            (" hello", " Welcome user"),
            (" close/exit", " End the program"),
        ]
        for command, description in commands:
            print("{:<20}|{:<50}".format(command, description))
