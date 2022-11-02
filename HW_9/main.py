import sys

from parser import user_command_parser
from handler import handlers, error_command_handler


def main():
    while True:
        user_command = input('Please enter command:')
        result = user_command_parser(user_command=user_command)
        if len(result) != 2:
            print(result)
            continue
        command, arguments = result
        command_handler = handlers.get(command, error_command_handler)

        try:
            command_response = command_handler(*arguments)
            print(command_response)
        except SystemExit as e:
            print(e)
            break


if __name__ == "__main__":
    main()