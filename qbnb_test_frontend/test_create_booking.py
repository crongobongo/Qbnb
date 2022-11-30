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
    
    # test create booking function
    # Blackbox Testing Method 1 - Input Partition Test
    def test_create_booking_input_email1_failure(self, *_):

        # register test user
        self.open(base_url + '/register')
        self.type("#email", "santiago@gmail.com")
        self.type("#name", "santiago")
        self.type("#password", "100Santiago!")
        self.type("#password2", "100Santiago!")
        self.click('input[type="submit"]')

        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        self.type("#title", "New House A")
        self.type("#description", "Welcome to this very nice new big house")
        self.type("#price", 1000)
        self.type("#last_modified_date", "2022-11-11")
        self.type("#email", "santiago@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        # user email and owner email are the same
        self.type("#user_email", "santiago@gmail.com")
        self.type("#listing_title", "New House A")
        self.type("#start_date", "2022-11-12")
        self.type("#end_date", "2022-11-13")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Cannot book y=our own listing!", 
        "#create-booking-header")

    def test_create_booking_input_email2_failure(self, *_):
        
        # register a new user
        self.open(base_url + '/register')
        self.type("#email", "cachamo@gmail.com")
        self.type("#name", "cachamo")
        self.type("#password", "100Cachamo!")
        self.type("#password2", "100Cachamo!")
        self.click('input[type="submit"]')

        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        # user email does not exist
        self.type("#user_email", "jskdfjsd@gmail.com")
        self.type("#listing_title", "New House A")
        self.type("#start_date", "2022-11-12")
        self.type("#end_date", "2022-11-13")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Creation Failed.", "#create-booking-header")

    def test_create_booking_input_title_failure(self, *_):

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        # listing title does not exist
        self.type("#user_email", "cachamo@gmail.com")
        self.type("#listing_title", "New House sfd")
        self.type("#start_date", "2022-11-12")
        self.type("#end_date", "2022-11-13")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Creation Failed.", "#create-booking-header")

    def test_create_booking_input_success(self, *_):

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        # create a successful booking
        self.type("#user_email", "cachamo@gmail.com")
        self.type("#listing_title", "New House A")
        self.type("#start_date", "2022-11-12")
        self.type("#end_date", "2022-11-14")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Created.", "#create-booking-header")

    def test_create_booking_input_date_failure(self, *_):

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        # booking dates overlap
        self.type("#user_email", "cachamo@gmail.com")
        self.type("#listing_title", "New House A")
        self.type("#start_date", "2022-11-13")
        self.type("#end_date", "2022-11-14")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Invalid booking date.", "#create-booking-header")