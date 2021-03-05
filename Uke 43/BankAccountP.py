class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):    # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self._first_name
        last = self._last_name
        number = self._number
        bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)

    def transfer(self, rec_acc, amount):
        self._balance -= amount
        rec_acc.deposit(amount)


def test_bank_class():
    a1 = BankAccountP("Cory", "Balaton", "19948375543", 10000)
    a2 = BankAccountP("Sofie", "Bragnes", "48274942479", 10000)

    e = 10**-6

    calculated = a1.get_balance()
    expected = 10000
    assert abs(calculated - expected) < e

    a1.deposit(1000)
    calculated = a1.get_balance()
    expected = 11000
    assert abs(calculated - expected) < e

    a1.withdraw(1000)
    calculated = a1.get_balance()
    expected = 10000
    assert abs(calculated - expected) < e

    a1.transfer(a2, 1000)
    calculated1 = a1.get_balance()
    expected1 = 9000
    calculated2 = a2.get_balance()
    expected2 = 11000
    assert abs(calculated1 - expected1) < e \
        and abs(calculated2 - expected2) < e


test_bank_class()

'''
(base) corybalaton@Corys-MacBook-Pro Uke 43 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Uke 43/BankAccountP.py"
'''
