'''CLASS deep diving
    (1) ENCAPSULATION <
    (2) INHERITENCE
    (3) POLIMORPHISM
'''

print("===== ENCAPSULATION =====")
# ENCAPSULATION > public __private _protected


class Account():
    description = "The class makes bank accounts"

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    def my_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} won")

    def deposit(self, amount):
        print("deposit", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw", amount)
        self.__amount -= amount

    @property   # decorator
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change ownership", new_owner)
        self.__owner = new_owner


my_account = Account("Mason", 2000)
my_account.my_balance()

my_account.deposit(2500)
my_account.withdraw(1000)
my_account.my_balance()


print("_________")

try:
    result = my_account.__amount
    print("result", result)
except Exception as err:
    print("No target state found:", err)

print("owner before", my_account.holder)  # state
# my_account.change_ownership("Gabriel")
my_account.holder = "Gabriel"  # state
print("owner after", my_account.holder)
