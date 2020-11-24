import unittest
from user import User
import pyperclip


class testUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        """
        Method to run before each test case
        """
        
        self.new_user = User("Maranatha", "uwase", "Marah-uwase", "marahuwase@31998") # Create user object
        
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Maranatha")
        self.assertEqual(self.new_user.last_name,"uwase")
        self.assertEqual(self.new_user.user_name,"Marah-uwase")
        self.assertEqual(self.new_user.password,"marahuwase@31998") 

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''

            User.user_list = []

    def test_save_multiple_users(self):

        '''
        test_save_multiple_users to check if we can save multiple user
        objects to our user_list
        '''
        
        self.new_user.save_user()
        test_user = User("moza", "mwenge", "mMrah_afr", "marah@31998")
        test_user.save_user() 
        self.assertEqual(len(User.user_list),2) 

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''

        self.new_user.save_user()
        test_user = User("Lupita", "Nyongo'o", "Lupita", "blackis beautiful")
        test_user.save_user()

        self.new_user.delete_user() #Deleting a user object
        self.assertEqual(len(User.user_list),1)
          
    
    def test_find_by_username(self):
        '''
        test to check if we can find a user by their username and display infformation
        '''
        self.new_user.save_user()
        test_user = User("Lupita", "Nyongo'o", "Lupita", "blackis beautifull")
        test_user.save_user()

        found_user = User.find_by_username("Lupita")
        self.assertEqual(found_user.user_name,"Lupita")


    def test_find_by_password(self):
        '''
        test to check if we can find a user by their password
        
        '''

        self.new_user.save_user()
        test_user = User("cheki", "ninah", "Gloria", "gloire")
        test_user.save_user()

        found_password = User.find_by_userpassword("gloire")
        self.assertEqual(found_password.password,"gloire")    
       
    

    def test_display_user_information(self):
        '''
        test to check if we can be able to display users saved in user_list
        '''

        self.assertEqual(User.display_userInfo(),User.user_list)




if __name__ == '__main__':
    unittest.main()
