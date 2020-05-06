from abc import ABC, abstractclassmethod
from OOP.bank.real_time import RealTime
from OOP.bank.log import Log
from time import sleep


class Account(ABC, Log):

    def __init__(self, branch, number, holder, balance):
        self._branch = branch
        self._number = number
        self._holder = holder
        self._balance = balance

    @property
    def number(self):
        return self._number

    @property
    def holder(self):
        return self._holder

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def transfer(self, amount, target_account):
        self.withdrawal(amount, name=self.holder)
        target_account.deposit(amount)
        print(f'Transfering €{amount} from {self.__class__.__name__} Account to {target_account} Account... ...')
        sleep(2)
        print('Transfer successful')

    def details(self):
        print(f'Branch: {self._branch}', end='\n')
        print(f'Customer name: {self.holder}', end='\n')
        print(f'Account Type: {self.__class__.__name__}', end='\n')
        print(f'Account No.: {self.number}', end='\n')
        print(f'Balance: €{self.balance}')

    def _check_balance(self, amount, limit=0):
        amount_available = self.balance + limit
        return amount <= amount_available

    def _change_balance(self, amount):
        print('Please wait while we are processing your request...')
        sleep(1)
        self._balance -= amount
        self.log_info(f'€{amount} has been withdrawn from your {self.number} account. @{RealTime.realtime()}')

    @abstractclassmethod
    def withdrawal(cls, amount, name): pass
