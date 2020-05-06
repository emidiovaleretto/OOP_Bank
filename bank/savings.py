from OOP.bank.account import Account


class Savings(Account):

    def withdrawal(self, amount, name):
        if name != self.holder:
            print(f'{name} is not the account holder. Please try again.')
            return
        if self._check_balance(amount):
            self._change_balance(amount)
        else:
            self.log_error(f'Error: Insufficient withdrawable funds. The account number {self.number} '
                           f'does not have enough funds.')
            return
