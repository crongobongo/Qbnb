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
        self.assert_text("Booking Creation Failed.", "#create-booking-header")

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

    def test_create_booking_input_date_failure(self, *_):

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        # booking dates overlap
        self.type("#user_email", "cachamo@gmail.com")
        self.type("#listing_title", "New House A")
        self.type("#start_date", "2022-11-13")
        self.type("#end_date", "2022-11-12")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Creation Failed.", "#create-booking-header")

    def test_create_booking_input_success(self, *_):

        # navigate to create booking page
        self.open(base_url + '/register')
        self.type("#email", "frank00@email.com")
        self.type("#name", "frank00")
        self.type("#password", "abC12!")
        self.type("#password2", "abC12!")
        self.click('input[type="submit"]')

        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # navigate to create listing page
        self.open(base_url + '/create_listing')
        # title contains leading space
        self.type("#title", "Small House")
        self.type("#description", "This is a new nice big house")
        self.type("#price", 100)
        self.type("#last_modified_date", "2022-01-01")
        self.type("#email", "frank00@email.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

        # navigate to create booking page
        self.open(base_url + '/register')
        self.type("#email", "tommy18@email.com")
        self.type("#name", "tommy18")
        self.type("#password", "abC12!")
        self.type("#password2", "abC12!")
        self.click('input[type="submit"]')

        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        self.open(base_url + '/create_booking')
        self.type("#user_email", "tommy18@email.com")
        self.type("#listing_title", "Small House")
        self.type("#start_date", "2022-01-06")
        self.type("#end_date", "2022-01-09")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Created.", "#create-booking-header")
    ######################################################

    # Output Partition Testing
    ######################################################
    def test_create_booking_output_success(self, *_):
        # navigate to create listing page
        self.open(base_url + '/create_listing')
        self.type("#title", "BEEDOW HOSE")
        self.type("#description", "This is a new nice big house")
        self.type("#price", 100)
        self.type("#last_modified_date", "2022-01-01")
        self.type("#email", "santiago@gmail.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

        # navigate to create booking page
        self.open(base_url + '/create_booking')
        self.type("#user_email", "cachamo@gmail.com")
        self.type("#listing_title", "BEEDOW HOSE")
        self.type("#start_date", "2022-01-06")
        self.type("#end_date", "2022-01-09")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Created.", "#create-booking-header")
    
    def test_create_booking_output_failure(self, *_):
        # navigate to create booking page
        self.open(base_url + '/create_booking')
        self.type("#user_email", "cachamo@gmail.com")
        self.type("#listing_title", "BEEDOW HOSE")
        self.type("#start_date", "2022-01-06")
        self.type("#end_date", "2022-01-09")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Creation Failed.", "#create-booking-header")
    ######################################################

    # Functionality Testing
    ######################################################
    def test_create_booking_functionality_success(self, *_):
        # register an owner
        self.open(base_url + '/register')
        self.type("#email", "frank01@email.com")
        self.type("#name", "frank01")
        self.type("#password", "abC12!")
        self.type("#password2", "abC12!")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # create a listing
        self.open(base_url + '/create_listing')
        self.type("#title", "OHIO House")
        self.type("#description", "This is a new nice big house")
        self.type("#price", 100)
        self.type("#last_modified_date", "2022-01-01")
        self.type("#email", "frank01@email.com")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-listing-header")
        self.assert_text("Listing Created.", "#create-listing-header")

        # register a user
        self.open(base_url + '/register')
        self.type("#email", "bengo3022@email.com")
        self.type("#name", "bengo3022")
        self.type("#password", "abC12!")
        self.type("#password2", "abC12!")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

        # create a booking
        self.open(base_url + '/create_booking')
        self.type("#user_email", "bengo3022@email.com")
        self.type("#listing_title", "OHIO House")
        self.type("#start_date", "2022-01-06")
        self.type("#end_date", "2022-01-09")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Created.", "#create-booking-header")

    def test_create_booking_functionality_failure(self, *_):
        # create a booking
        self.open(base_url + '/create_booking')
        self.type("#user_email", "bengo3022@email.com")
        self.type("#listing_title", "OHIO House")
        self.type("#start_date", "2022-01-06")
        self.type("#end_date", "2022-01-09")
        self.click('input[type="submit"]')
        time.sleep(1)  # page should load correctly
        self.assert_element("#create-booking-header")
        self.assert_text("Booking Creation Failed.", "#create-booking-header")
    ######################################################