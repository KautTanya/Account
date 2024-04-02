"""Account"""


class Account:
    """Account"""
    def __init__(self, balance, account_holder):
        self.__balance = balance
        self._account_holder = account_holder

    def get_balance(self):
        """balance"""
        return self.__balance

    def get_account_holder(self):
        """account_holder"""
        return self._account_holder


account = Account(1000, "Jack")

print(account.get_balance())
print(account.get_account_holder())
