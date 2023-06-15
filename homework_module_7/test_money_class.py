from unittest import TestCase, main
from money_class import Money


class TestMoney(TestCase):
    def test_plus(self):
        money_1 = Money(100)
        self.assertEqual(money_1 + 10, 110)

    def test_minus(self):
        money_2 = Money(500)
        self.assertEqual(money_2 - 150.5, 349.5)

    def test_equal(self):
        money_3 = Money(1000.5)
        self.assertEqual(money_3, 1000.5)

    def test_not_equal(self):
        money_4 = Money(7892.645)
        self.assertNotEqual(money_4, 7893.645)

    def test_incorrect_set_balance(self):
        with self.assertRaises(ValueError) as e:
            money_5 = Money(-100)
        self.assertEqual('The balance must be greater than or equal to 0!', e.exception.args[0])

    def test_subtraction_give_negative_balance(self):
        with self.assertRaises(ValueError) as e:
            money_6 = Money(50)
            money_6 - 100
        self.assertEqual('It is impossible to subtract your value from the balance. You entered too large number',
                         e.exception.args[0])

    def test_adding_incorrect_type(self):
        with self.assertRaises(TypeError) as e:
            money_7 = Money(200)
            money_7 + '150'
        self.assertEqual('It is not possible to add your value to the balance. Please enter a numeric value!',
                         e.exception.args[0])


if __name__ == '__main__':
    main()
