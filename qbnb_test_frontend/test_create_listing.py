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
    
    # test create listing function
    # Blackbox Testing Method 1 - Input Partition Test
    def test_create_listing_input_title1_failure(self, *_):

        # register test user
        self.open(base_url + '/register')
        self.type("#email", "chungus@gmail.com")
        self.type("#name", "chungus")
        self.type("#password", "100Chungus!")
        self.type("#password2", "100Chungus!")
        self.click('input[type="submit"]')

        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # title contains leading space
        self.type("#title", " New House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_title2_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # title contains trailing space
        self.type("#title", "New House ")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_title3_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # title exceeds character limit of 80
        self.type("#title", "Hey Peter" * 9)
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_title4_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # title contains non-alphanumeric characters
        self.type("#title", "New !><-+House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_desc1_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # description is less than 20 characters
        self.type("#title", "The Chungus House")
        self.type("#description", "This is Big Chungus")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_desc2_failure(self, *_):
        
        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # description length less than title length
        self.type("#title", "The Glorious Chungus House")
        self.type("#description", "This is the Chungus house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_desc3_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # description length exceeding 2000 characters
        self.type("#title", "The Chungus House")
        self.type("#description", "Big Chungus" * 182)
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")    

    def test_create_listing_input_price1_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # invalid price, too low
        self.type("#title", "The Fungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 2)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_price2_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # invalid price, too high
        self.type("#title", "The Fungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_price3_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # invalid price, not type int
        self.type("#title", "The Fungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", "yeet")
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Please enter an integer for price.", 
                         "#create-listing-header")

    def test_create_listing_input_email_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # invalid email, does not exist
        self.type("#title", "The Fungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungoooooo@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_date1_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # invalid date, before allowed date
        self.type("#title", "The Chungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2020-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_date2_failure(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # invalid date, after allowed date
        self.type("#title", "The Chungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2029-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_input_success(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # all requirements are met
        self.type("#title", "The Chungus House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

    # Blackbox Testing Method 2 - Output Partition Testing

    def test_create_listing_output_failure(self, *_):
        
        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # all requirements are met
        self.type("#title", " The <> House ")
        self.type("#description", "No")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2029-11-11")
        self.type("#email", "choochoo@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_output_price(self, *_):

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # all requirements are met
        self.type("#title", "The Chungus Yeet House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", "no")
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Please enter an integer for price.", 
                         "#create-listing-header")

    def test_create_listing_output_success(self, *_):
        
        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # all requirements are met
        self.type("#title", "The Chungus Feet House")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

    # Blackbox Testing Method 3 - Functionality Testing

    def test_create_listing_functionality_failure(self, *_):
        # Opens create listing page
        self.open(base_url + '/create_listing')
        self.type("#title", "  SpacesBeforeAndAfter  ")
        self.type("#description", "oh")
        self.type("#price", 3)
        self.type("#last_modified_date", "2009-11-11")
        self.type("#email", "notAReal@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Creation Failed.", "#create-listing-header")

    def test_create_listing_functionality_success(self, *_):
        # Opens create listing
        self.open(base_url + '/create_listing')
        self.type("#title", "Biggy Chungus")
        self.type("#description", "This is a complete description.")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "chungus@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # test if the page loads correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")