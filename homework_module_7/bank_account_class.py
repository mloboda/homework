import uuid
import logging


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city


class ContactInfo(Person, Address):
    def __init__(self, name, age, street, city):
        super(ContactInfo, self).__init__(name, age)
        Address.__init__(self, street, city)
        self.id = uuid.uuid1()

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Street: {self.street}, City: {self.city}, ID: {self.id}'


class Money:
    __amount = 0

    def __init__(self, amount=0):
        self.amount = amount

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if value >= 0:
            self.__amount = value
        else:
            raise ValueError('Amount must be a non-negative value')

    def __str__(self):
        return f'Amount: {self.__amount}'

    def __repr__(self):
        return f'Money: {self.__amount}'

    def top_up(self, amount):
        if amount > 0:
            self.__amount += amount
            self.logger.info(f'Your balance is replenished by {amount}')
        else:
            raise ValueError('Amount must be greater than 0')

    def withdraw(self, amount):
        if self.__amount >= amount > 0:
            self.__amount -= amount
            self.logger.info(f'{amount} withdrawn from your account')
        else:
            raise ValueError('There are not enough funds in the account or you entered a withdrawal amount less than 1')


class BankAccount:
    def __init__(self, contact_info):
        self.contact_info = contact_info
        self.balance = Money()


if __name__ == '__main__':
    contact_inform = ContactInfo('Maks', 20, 'Soborna Street', 'Vinnytsia')
    bank_account = BankAccount(contact_inform)

    print(bank_account.contact_info)
    bank_account.balance.top_up(1000)
    print(bank_account.balance)
    bank_account.balance.withdraw(500)
    print(bank_account.balance)

    try:
        bank_account.balance.withdraw(10000)
    except ValueError as ex:
        print(ex)
