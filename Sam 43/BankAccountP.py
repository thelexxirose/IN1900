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

    def transfer(self, amount, account):
        self._balance -= amount
        account.deposit(amount)

    def print_info(self):
        first = self._first_name
        last = self._last_name
        number = self._number
        bal = self._balance
        s = f'{first} {last}, {number}, balance: {bal}'
        print(s)


def test_BankAccountP_class():
    a1 = BankAccountP("Cory", "Balaton", 1654387469, 10000)
    a2 = BankAccountP("Samuel", "Bigirimana", 1854930049, 10000)

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

    a1.transfer(1000, a2)
    calculated_1 = a1.get_balance()
    expected_1 = 9000

    calculated_2 = a2.get_balance()
    expected_2 = 11000

    assert abs(calculated_1 - expected_1) < e \
        and abs(calculated_2 - expected_2) < e


test_BankAccountP_class()

'''
(base) corybalaton@Corys-MacBook-Pro Sam 43 %
/Users/corybalaton/opt/anaconda3/bin/python
"/Users/corybalaton/Documents/UiO/IN1900/Sam 43/BankAccountP.py"
'''
