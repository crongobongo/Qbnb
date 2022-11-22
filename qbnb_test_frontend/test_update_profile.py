from seleniumbase import BaseCase

from qbnb_test_frontend.conftest import base_url
from unittest.mock import patch
from qbnb.models import User
import qbnb
import time


"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    # Crete a user and listing
    def test_create_user(self, *_):
        self.open(base_url + '/register')
        self.type("#email", "will12@gmail.com")
        self.type("#name", "Will")
        self.type("#password", "Pingpong32@")
        self.type("#password2", "Pingpong32@")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    # Input Partition Testing
    def test_update_profile_input_old_email_failure(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "wiss12@gmail.com")
        self.type("#new_email", "markfark@gmail.com")
        self.type("#username", "willj")
        self.type("#billing_address", "123 hello")
        self.type("#postal_code", "M6R1K1")
        self.click('input[type="submit"]')
        time.sleep(1) 
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile update has failed.",
                         "#update-profile-header")

    def test_update_profile_input_new_email_failure(self, *_):
        self.open(base_url + '/register')
        self.type("#email", "davey13@gmail.com")
        self.type("#name", "davey")
        self.type("#password", "Dancey12@")
        self.type("#password2", "Dancey12@")
        self.click('input[type="submit"]')
        time.sleep(1) 
      
        self.open(base_url + '/update_profile')
        self.type("#old_email", "davey13@gmail.com")
        self.type("#new_email", "@s")
        self.type("#username", "dave")
        self.type("#billing_address", "12345 Home Street")
        self.type("#postal_code", "F3H7H3")
        self.click('input[type="submit"]')
        time.sleep(1) 
        self.assert_element("#update-profile-header")
    
    def test_update_profile_input_username_failure(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "will12@gmail.com")
        self.type("#username", "12")
        self.type("#billing_address", "123 hello")
        self.type("#postal_code", "M6R1K1")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile update has failed.", 
                         "#update-profile-header")

    def test_update_profile_input_postal_code_failure(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "will12@gmail.com")
        self.type("#username", "willj")
        self.type("#billing_address", "123 Hello")
        self.type("#postal_code", "H")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile update has failed.", 
                         "#update-profile-header")

    def test_update_profile_input_old_email_success(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "will12@gmail.com")
        self.type("#username", "willj12")
        self.type("#billing_address", "123 Hello")
        self.type("#postal_code", "M6R1K1")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    def test_update_profile_input_new_email_success(self, *_):
        self.open(base_url + '/register')
        self.type("#email", "donny12@gmail.com")
        self.type("#name", "donny")
        self.type("#password", "Pingpong323@")
        self.type("#password2", "Pingpong323@")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
        self.open(base_url + '/update_profile')
        self.type("#old_email", "donny12@gmail.com")
        self.type("#new_email", "markymark3@gmail.com")
        self.type("#username", "donny")
        self.type("#billing_address", "123 Hello")
        self.type("#postal_code", "M6R1K1")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    def test_update_profile_input_username_success(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "will12@gmail.com")
        self.type("#username", "dontoliver")
        self.type("#billing_address", "123 Hello")
        self.type("#postal_code", "M6R1K1")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    def test_update_profile_input_billing_address_success(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "will12@gmail.com")
        self.type("#username", "willj")
        self.type("#billing_address", "newmanstreet 123")
        self.type("#postal_code", "M6R1K1")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    def test_update_profile_input_postal_code_success(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "will12@gmail.com")
        self.type("#username", "will")
        self.type("#billing_address", "123 hello")
        self.type("#postal_code", "H7R9K9")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    # Output Partition Testing
    def test_update_profile_output_success(self, *_):
        self.open(base_url + '/register')
        self.type("#email", "david13@gmail.com")
        self.type("#name", "david")
        self.type("#password", "Dancey13@")
        self.type("#password2", "Dancey13@")
        self.click('input[type="submit"]')
        time.sleep(1) 
      
        self.open(base_url + '/update_profile')
        self.type("#old_email", "david13@gmail.com")
        self.type("#new_email", "willity12@gmail.com")
        self.type("#username", "willy")
        self.type("#billing_address", "1234 Home Street")
        self.type("#postal_code", "F2H7H3")
        self.click('input[type="submit"]')
        time.sleep(1) 
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    def test_update_profile_output_fail(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "willjiggity12@gmail.com")
        self.type("#username", "wi")
        self.type("#billing_address", "12")
        self.type("#postal_code", "13")
        self.click('input[type="submit"]')
        time.sleep(1)  
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile update has failed.", 
                         "#update-profile-header")

    # Functionality Testing

    def test_update_profile_functionality_success(self, *_):
        self.open(base_url + '/register')
        self.type("#email", "david12@gmail.com")
        self.type("#name", "davd")
        self.type("#password", "Dancey123@")
        self.type("#password2", "Dancey123@")
        self.click('input[type="submit"]')
        time.sleep(1) 
      
        self.open(base_url + '/update_profile')
        self.type("#old_email", "david12@gmail.com")
        self.type("#new_email", "willjiggity12@gmail.com")
        self.type("#username", "willy")
        self.type("#billing_address", "123 Home Street")
        self.type("#postal_code", "F1H7H3")
        self.click('input[type="submit"]')
        time.sleep(1) 
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile has been updated.", 
                         "#update-profile-header")

    def test_update_profile_functionality_fail(self, *_):
        self.open(base_url + '/update_profile')
        self.type("#old_email", "will12@gmail.com")
        self.type("#new_email", "willjigggity12@gmail.com")
        self.type("#username", "wi")
        self.type("#billing_address", "14")
        self.type("#postal_code", "131")
        self.click('input[type="submit"]')
        time.sleep(1) 
        self.assert_element("#update-profile-header")
        self.assert_text("User Profile update has failed.", 
                         "#update-profile-header")
