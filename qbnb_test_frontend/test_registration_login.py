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

    # test register function
    # input partition testing

    def test_registration_input_success(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "john100@gmail.com")
        self.type("#name", "john100")
        self.type("#password", "100John!")
        self.type("#password2", "100John!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_registration_input_email_failure(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "john200")
        self.type("#name", "john200")
        self.type("#password", "200John!")
        self.type("#password2", "200John!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_registration_input_name_failure(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "john300")
        self.type("#name", "john300!")
        self.type("#password", "300John!")
        self.type("#password2", "300John!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_registration_input_password_failure(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "john400")
        self.type("#name", "john400!")
        self.type("#password", "John!")
        self.type("#password2", "John!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_registration_input_password2_failure(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "john500")
        self.type("#name", "john500!")
        self.type("#password", "500John!")
        self.type("#password2", "5John!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    # output partition testing
    
    def test_registration_output_success(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "dave100@gmail.com")
        self.type("#name", "dave100")
        self.type("#password", "100Dave!")
        self.type("#password2", "100Dave!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_registration_output_registration_failed(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "dave200")
        self.type("#name", "dave200")
        self.type("#password", "200Dave!")
        self.type("#password2", "200Dave!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_registration_output_passwords_not_match(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "dave200@gmail.com")
        self.type("#name", "dave200")
        self.type("#password", "Dave!")
        self.type("#password2", "100Dave!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    # Functionality Testing 

    def test_registration_functionality_success(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "Steve100@gmail.com")
        self.type("#name", "steve100")
        self.type("#password", "100Steve!")
        self.type("#password2", "100Steve!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_registration_functionality_registration_failed(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "Steve200")
        self.type("#name", "Steve200")
        self.type("#password", "200Steve!")
        self.type("#password2", "200Steve!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Registration failed.", "#message")

    def test_registration_functionality_passwords_not_match(self, *_):
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "Steve200@gmail.com")
        self.type("#name", "Steve200")
        self.type("#password", "Steve!")
        self.type("#password2", "200Steve!")
        # click enter button
        self.click('input[type="submit"]')

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")    

    # test login function
    # input partition testing

    def test_login_input_success(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "paul100@gmail.com")
        self.type("#name", "paul100")
        self.type("#password", "100Paul!")
        self.type("#password2", "100Paul!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "paul100@gmail.com")  # type email
        self.type("#password", "100Paul!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome paul100 !", "#welcome-header")

    def test_login_input_email_failure(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "paul200@gmail.com")
        self.type("#name", "paul200")
        self.type("#password", "200Paul!")
        self.type("#password2", "200Paul!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "paul@gmail.com")  # type email
        self.type("#password", "200Paul!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text('login failed', "#message")

    def test_login_input_password_failure(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "paul300@gmail.com")
        self.type("#name", "paul300")
        self.type("#password", "300Paul!")
        self.type("#password2", "300Paul!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "paul300@gmail.com")  # type email
        self.type("#password", "Paul!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text('login failed', "#message") 

    # output partition testing 

    def test_login_output_success(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "judy100@gmail.com")
        self.type("#name", "judy100")
        self.type("#password", "100Judy!")
        self.type("#password2", "100Judy!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "judy100@gmail.com")  # type email
        self.type("#password", "100Judy!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome judy100 !", "#welcome-header")

    def test_login_output_failure(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "judy200@gmail.com")
        self.type("#name", "judy200")
        self.type("#password", "200Judy!")
        self.type("#password2", "200Judy!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "judy@gmail.com")  # type email
        self.type("#password", "200Judy!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text('login failed', "#message")  

    # Functionality Testing          

    def test_login_functionality_success(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "taco100@gmail.com")
        self.type("#name", "taco100")
        self.type("#password", "100Taco!")
        self.type("#password2", "100Taco!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "taco100@gmail.com")  # type email
        self.type("#password", "100Taco!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome taco100 !", "#welcome-header")

    def test_login_functionality_failure(self, *_):
        # register test user
        self.open(base_url + '/register')
        self.type("#email", "taco200@gmail.com")
        self.type("#name", "taco200")
        self.type("#password", "200Taco!")
        self.type("#password2", "200Taco!")
        # load login page
        self.click('input[type="submit"]')

        self.type("#email", "taco")  # type email
        self.type("#password", "200Taco!")  # type password
        self.click('input[type="submit"]')  # click submit

        time.sleep(1)
        # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text('login failed', "#message")