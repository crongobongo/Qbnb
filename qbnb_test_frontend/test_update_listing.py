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
    def test_create_user_and_listing(self, *_):
        # open register page
        self.open(base_url + '/register')
        # create user
        self.type("#email", "bengo3022@gmail.com")
        self.type("#name", "Benjamin")
        self.type("#password", "Password420!")
        self.type("#password2", "Password420!")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # create listing
        self.open(base_url + '/create_listing')
        self.type("#title", "BrittleStack")
        self.type("#description", "Stackin up the brittles.")
        self.type("#price", "800")
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "bengo3022@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

    # Input Partition Testing
    ######################################################
    def test_update_listing_input_email_failure(self, *_):
        # Opens update listing page and inputs wrong email
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo300000002@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Update Failed.", "#update-listing-header")

    def test_update_listing_input_title_failure(self, *_):
        # Opens update listing page and inputs wrong title
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "  BimbleStack  ")
        self.type("#description", "N/A")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Update Failed.", "#update-listing-header")
        
    def test_update_listing_input_description_failure(self, *_):
        # Opens update listing page and inputs wrong description
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "ah")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Update Failed.", "#update-listing-header")
    
    def test_update_listing_input_price_failure(self, *_):
        # Opens update listing page and inputs wrong price
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "700")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Update Failed.", "#update-listing-header")

    def test_update_listing_input_email_success(self, *_):
        # Opens update listing page and inputs correct email
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Updated.", "#update-listing-header")

    def test_update_listing_input_title_success(self, *_):
        # Opens update listing page and inputs correct title
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "BrittlePacks")
        self.type("#description", "N/A")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Updated.", "#update-listing-header")

    def test_update_listing_input_description_success(self, *_):
        # Opens update listing page and inputs correct description
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "I can't stop stacking up the bricks man.")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Updated.", "#update-listing-header")

    def test_update_listing_input_price_success(self, *_):
        # Opens update listing page and inputs correct price
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "900")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Updated.", "#update-listing-header")
    ######################################################

    # Output Partition Testing
    ######################################################
    def test_update_listing_output_failure(self, *_):
        # Opens update listing page to recieve "Listing Update Failed." output
        self.open(base_url + '/update_listing')
        self.type("#email", "notAReal@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "-1")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Update Failed.", "#update-listing-header")
        
    def test_update_listing_output_success(self, *_):
        # Opens update listing page to recieve "Listing Updated." output
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "2000")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Updated.", "#update-listing-header")

    def test_update_listing_output_price(self, *_):
        # Opens update listing page to recieve
        # "Please enter an integer for price." output
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "N/A")
        self.type("#description", "N/A")
        self.type("#price", "ADA")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Please enter an integer for price.",
                         "#update-listing-header")
    ######################################################

    # Functionality Testing
    ######################################################
    def test_update_listing_functionality_failure(self, *_):
        # Opens update listing page
        # Updates all attributes incorrectly
        self.open(base_url + '/update_listing')
        self.type("#email", "notAReal@gmail.com")
        self.type("#title", "  SpacesBeforeAndAfter  ")
        self.type("#description", "oh")
        self.type("#price", "3")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Update Failed.", "#update-listing-header")

    def test_update_listing_functionality_success(self, *_):
        # Opens update listing
        # Updates all attributes correctly
        self.open(base_url + '/update_listing')
        self.type("#email", "bengo3022@gmail.com")
        self.type("#title", "ValidTitle")
        self.type("#description", "This is a completely valid description.")
        self.type("#price", "5000")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#update-listing-header")
        self.assert_text("Listing Updated.", "#update-listing-header")
    ######################################################