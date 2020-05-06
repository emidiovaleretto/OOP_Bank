from OOP.bank.account import Account


class Current(Account):

    def __init__(self, branch, number, holder, balance, limit=200):
        super().__init__(branch, number, holder, balance)
        self._limit = limit

    def withdrawal(self, amount, name):
        if name != self._holder:
            print(f'{name} is not the account holder. Please try again.')
        else:
            if self._check_balance(amount, self._limit):
                self._change_balance(amount)
            else:
                self.log_error(f'Error: Insufficient withdrawable funds. The account number {self.number} '
                               f'does not have enough funds.')
                return
