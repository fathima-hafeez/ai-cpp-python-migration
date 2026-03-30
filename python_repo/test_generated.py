import unittest
from account import Account
from bank_system import BankSystem


class TestAccountInit(unittest.TestCase):

    def test_init_sets_id(self):
        acc = Account(1, 500)
        self.assertEqual(acc.id, 1)

    def test_init_sets_balance(self):
        acc = Account(1, 500)
        self.assertEqual(acc.balance, 500)

    def test_init_with_zero_balance(self):
        acc = Account(2, 0)
        self.assertEqual(acc.balance, 0)

    def test_init_with_negative_balance(self):
        acc = Account(3, -100)
        self.assertEqual(acc.balance, -100)

    def test_init_with_float_balance(self):
        acc = Account(4, 99.99)
        self.assertAlmostEqual(acc.balance, 99.99)

    def test_init_with_string_id(self):
        acc = Account("ACC001", 200)
        self.assertEqual(acc.id, "ACC001")

    def test_init_with_large_balance(self):
        acc = Account(5, 10 ** 9)
        self.assertEqual(acc.balance, 10 ** 9)

    def test_init_with_zero_id(self):
        acc = Account(0, 100)
        self.assertEqual(acc.id, 0)


class TestAccountDeposit(unittest.TestCase):

    def test_deposit_positive_amount(self):
        acc = Account(1, 1000)
        acc.deposit(200)
        self.assertEqual(acc.balance, 1200)

    def test_deposit_zero_amount(self):
        acc = Account(1, 1000)
        acc.deposit(0)
        self.assertEqual(acc.balance, 1000)

    def test_deposit_negative_amount(self):
        acc = Account(1, 1000)
        acc.deposit(-200)
        self.assertEqual(acc.balance, 800)

    def test_deposit_float_amount(self):
        acc = Account(1, 100)
        acc.deposit(50.50)
        self.assertAlmostEqual(acc.balance, 150.50)

    def test_deposit_multiple_times(self):
        acc = Account(1, 0)
        acc.deposit(100)
        acc.deposit(200)
        acc.deposit(300)
        self.assertEqual(acc.balance, 600)

    def test_deposit_large_amount(self):
        acc = Account(1, 0)
        acc.deposit(10 ** 9)
        self.assertEqual(acc.balance, 10 ** 9)

    def test_deposit_updates_balance_correctly_from_zero(self):
        acc = Account(1, 0)
        acc.deposit(500)
        self.assertEqual(acc.balance, 500)

    def test_deposit_from_negative_balance(self):
        acc = Account(1, -500)
        acc.deposit(300)
        self.assertEqual(acc.balance, -200)

    def test_deposit_brings_balance_to_zero(self):
        acc = Account(1, -500)
        acc.deposit(500)
        self.assertEqual(acc.balance, 0)

    def test_deposit_does_not_change_id(self):
        acc = Account(42, 100)
        acc.deposit(50)
        self.assertEqual(acc.id, 42)


class TestAccountGetBalance(unittest.TestCase):

    def test_get_balance_returns_initial_balance(self):
        acc = Account(1, 1000)
        self.assertEqual(acc.get_balance(), 1000)

    def test_get_balance_after_deposit(self):
        acc = Account(1, 1000)
        acc.deposit(200)
        self.assertEqual(acc.get_balance(), 1200)

    def test_get_balance_with_zero_balance(self):
        acc = Account(1, 0)
        self.assertEqual(acc.get_balance(), 0)

    def test_get_balance_with_negative_balance(self):
        acc = Account(1, -300)
        self.assertEqual(acc.get_balance(), -300)

    def test_get_balance_with_float_balance(self):
        acc = Account(1, 99.99)
        self.assertAlmostEqual(acc.get_balance(), 99.99)

    def test_get_balance_does_not_modify_balance(self):
        acc = Account(1, 500)
        acc.get_balance()
        acc.get_balance()
        self.assertEqual(acc.get_balance(), 500)

    def test_get_balance_reflects_multiple_deposits(self):
        acc = Account(1, 0)
        acc.deposit(100)
        acc.deposit(150)
        acc.deposit(250)
        self.assertEqual(acc.get_balance(), 500)

    def test_get_balance_returns_correct_type_int(self):
        acc = Account(1, 100)
        self.assertIsInstance(acc.get_balance(), int)

    def test_get_balance_returns_correct_type_float(self):
        acc = Account(1, 100.5)
        self.assertIsInstance(acc.get_balance(), float)


class TestBankSystemInit(unittest.TestCase):

    def test_init_creates_empty_accounts_list(self):
        bank = BankSystem()
        self.assertEqual(bank.accounts, [])

    def test_init_accounts_is_list(self):
        bank = BankSystem()
        self.assertIsInstance(bank.accounts, list)

    def test_multiple_instances_have_independent_accounts(self):
        bank1 = BankSystem()
        bank2 = BankSystem()
        bank1.accounts.append(Account(1, 100))
        self.assertEqual(len(bank2.accounts), 0)


class TestBankSystemAddAccount(unittest.TestCase):

    def test_add_account_increases_list_length(self):
        bank = BankSystem()
        acc = Account(1, 500)
        bank.add_account(acc)
        self.assertEqual(len(bank.accounts), 1)

    def test_add_account_stores_correct_account(self):
        bank = BankSystem()
        acc = Account(1, 500)
        bank.add_account(acc)
        self.assertIs(bank.accounts[0], acc)

    def test_add_multiple_accounts(self):
        bank = BankSystem()
        acc1 = Account(1, 100)
        acc2 = Account(2, 200)
        acc3 = Account(3, 300)
        bank.add_account(acc1)
        bank.add_account(acc2)
        bank.add_account(acc3)
        self.assertEqual(len(bank.accounts), 3)

    def test_add_multiple_accounts_order_preserved(self):
        bank = BankSystem()
        acc1 = Account(1, 100)
        acc2 = Account(2, 200)
        bank.add_account(acc1)
        bank.add_account(acc2)
        self.assertIs(bank.accounts[0], acc1)
        self.assertIs(bank.accounts[1], acc2)

    def test_add_account_with_zero_balance(self):
        bank = BankSystem()
        acc = Account(1, 0)
        bank.add_account(acc)
        self.assertEqual(bank.accounts[0].get_balance(), 0)

    def test_add_account_with_negative_balance(self):
        bank = BankSystem()
        acc = Account(1, -100)
        bank.add_account(acc)
        self.assertEqual(bank.accounts[0].get_balance(), -100)

    def test_add_account_does_not_duplicate_on_single_call(self):
        bank = BankSystem()
        acc = Account(1, 100)
        bank.add_account(acc)
        self.assertEqual(len(bank.accounts), 1)

    def test_add_same_account_twice(self):
        bank = BankSystem()
        acc = Account(1, 100)
        bank.add_account(acc)
        bank.add_account(acc)
        self.assertEqual(len(bank.accounts), 2)
        self.assertIs(bank.accounts[0], bank.accounts[1])

    def test_add_account_account_is_accessible_after_add(self):
        bank = BankSystem()
        acc = Account(99, 750)
        bank.add_account(acc)
        retrieved = bank.accounts[0]
        self.assertEqual(retrieved.id, 99)
        self.assertEqual(retrieved.get_balance(), 750)

    def test_add_account_balance_updates_reflect_in_bank(self):
        bank = BankSystem()
        acc = Account(1, 100)
        bank.add_account(acc)
        acc.deposit(400)
        self.assertEqual(bank.accounts[0].get_balance(), 500)

    def test_add_account_none_value(self):
        bank = BankSystem()
        bank.add_account(None)
        self.assertIsNone(bank.accounts[0])

    def test_add_account_non_account_object(self):
        bank = BankSystem()
        bank.add_account("not_an_account")
        self.assertEqual(bank.accounts[0], "not_an_account")


class TestIntegration(unittest.TestCase):

    def test_deposit_then_get_balance(self):
        acc = Account(1, 1000)
        acc.deposit(200)
        self.assertEqual(acc.get_balance(), 1200)

    def test_main_scenario(self):
        acc1 = Account(1, 1000)
        acc1.deposit(200)
        self.assertEqual(acc1.get_balance(), 1200)

    def test_bank_system_with_account_operations(self):
        bank = BankSystem()
        acc = Account(1, 500)
        bank.add_account(acc)
        bank.accounts[0].deposit(300)
        self.assertEqual(bank.accounts[0].get_balance(), 800)

    def test_multiple_accounts_independent_balances(self):
        bank = BankSystem()
        acc1 = Account(1, 100)
        acc2 = Account(2, 200)
        bank.add_account(acc1)
        bank.add_account(acc2)
        bank.accounts[0].deposit(50)
        self.assertEqual(bank.accounts[0].get_balance(), 150)
        self.assertEqual(bank.accounts[1].get_balance(), 200)

    def test_full_workflow(self):
        bank = BankSystem()
        for i in range(5):
            acc = Account(i, i * 100)
            bank.add_account(acc)
        self.assertEqual(len(bank.accounts), 5)
        bank.accounts[2].deposit(500)
        self.assertEqual(bank.accounts[2].get_balance(), 700)


if __name__ == "__main__":
    unittest.main()