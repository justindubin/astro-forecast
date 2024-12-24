import os

from src.configuration import load_env_vars


class Messenger:

    def __init__(self):
        load_env_vars()

    @staticmethod
    def send_test_message(body: str) -> None:
        pass


if __name__ == "__main__":
    messenger = Messenger()
    messenger.send_test_message(body='This is a test of the Textbelt freemium service')
