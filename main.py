from cryptography.fernet import Fernet


class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()  # BASE-64 encryption
        with open(path, 'wb') as file:
            file.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as file:
            self.key = file.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, values in initial_values.items():



def main():
    pm = PasswordManager()
    pm.create_key("mykey.key")  # TODO: check file path values None/Undefined


if __name__ == "__main__":
    main()