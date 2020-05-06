from OOP.bank.bank import Bank

class Client(Bank):

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.account = None
        self.client = None

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def insert_account(self, account):
        self.account = account

    def insert_client(self, client):
        self.client = client

    def __repr__(self):
        return f'{self.name}'
