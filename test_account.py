import unittest
from account import Account

class TestAccount(unittest.TestCase):
    
    def setUp(self):
        self.new_account = Account ("twiter","Marah_afr","marah@31998" )
    
    def test__init__(self):
        """
        Check if a  class was initialsed
        """
    def test_init(self):
        self.assertEqual(self.new_account.account_name,"twiter")
        self.assertEqual(self.new_account.account_userName,"Marah_afr")
        self.assertEqual(self.new_account.account_password,"marah@31998")
        pass
    
    def test_save_account(self):
        self.new_account.save_account() #saving the new account
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
        Account.account_list = []

    def test_display_account_credentials(self):
        self.assertEqual(Account.display_accounts(),Account.account_list)

    def test_delete_account(self):
        self.new_account.save_account()
        test_account = Account("Twitter", "nakia", "moviesarebae")
        test_account.save_account()

        test_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_name(self):
        self.new_account.save_account()
        test_account = Account("Twitter", "Kevin_hartz", "jumanji")
        test_account.save_account()

        found_account = Account.find_by_accountName("Twitter")
        self.assertEqual(found_account.account_name,"Twitter")


if __name__ == '__main__':
    unittest.main()