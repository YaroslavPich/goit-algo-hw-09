from controller import AddressBookController
from view import ConsoleAddressBookView


def main():
    controller = AddressBookController()
    view = ConsoleAddressBookView()
    view.display_message("Welcome to the assistant bot!")
    view.display_message("Enter 'command' to see options!")
    controller.load_data()
    while True:
        user_input = input("Enter a command: ")
        if user_input.strip().lower() in ("close", "exit"):
            controller.command(user_input)
            break
        controller.command(user_input)
    controller.save_data()


if __name__ == "__main__":
    main()
