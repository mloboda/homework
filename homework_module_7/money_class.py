class Money:
    __balance = 0

    def __init__(self, balance=0):
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if isinstance(balance, (int, float)):
            if balance >= 0:
                self.__balance = balance
            else:
                raise ValueError('The balance must be greater than or equal to 0!')
        else:
            raise TypeError('You entered an invalid value, you can only set a numeric value!')

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.__balance == other
        else:
            raise TypeError('It is not possible to compare a number with your value. Please enter a numeric value!')

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.__balance != other
        else:
            raise TypeError('It is not possible to compare a number with your value. Please enter a numeric value!')

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.__balance += other
            return self.__balance
        else:
            raise TypeError('It is not possible to add your value to the balance. Please enter a numeric value!')

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            if self.__balance > other:
                self.__balance -= other
                return self.__balance
            else:
                raise ValueError(
                    'It is impossible to subtract your value from the balance. You entered too large number')
        else:
            raise TypeError('You entered an invalid value, you can only set a numeric value!')
