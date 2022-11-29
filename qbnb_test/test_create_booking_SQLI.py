from qbnb.models import register
from qbnb.models import create_listing
from qbnb.models import create_booking
import random
import string


def test_user_email_create_booking():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers an owner
    register("owner", "owner@gmail.com", "Abc12!")
    title = "Title#"
    # Counter for different titles and users
    num = 0
    # Goes through each line
    for line in text:
        # Creates and registers a user for each line
        user_email = line.strip() + "@gmail.com"
        register("user" + str(num), user_email, "Abc12!")
        # Creates a listing
        temp_title = title + str(num)
        create_listing(temp_title, "A very valid description.", 800,
                       "2022-11-11", "owner@gmail.com")
        # Test to see if it creates the booking
        # (with a different listing each time)
        try:
            create_booking(user_email, temp_title, "2022-11-12", "2022-11-13")
        except Exception():
            print("An error occurred")
        num += 1
    file1.close()


def test_listing_title_create_booking():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers an owner
    register("owner2", "owner2@gmail.com", "Abc12!")
    # Counter for different titles and users
    num = 0
    # Goes through each line
    for line in text:
        listing_title = line.strip()
        # Creates and registers a user for each line
        user_email = "anotheruser" + str(num) + "@gmail.com"
        register("anotheruser" + str(num), user_email, "Abc12!")
        # Creates a listing
        create_listing(listing_title, "A very valid description.", 800,
                       "2022-11-11", "owner2@gmail.com")
        # Test to see if it creates the booking
        # (with a different listing each time)
        try:
            create_booking(user_email, listing_title,
                           "2022-11-12", "2022-11-13")
        except Exception():
            print("An error occurred")
        num += 1
    file1.close()


def test_start_date_create_booking():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers an owner
    register("owner3", "owner3@gmail.com", "Abc12!")
    title = "NiceTitle#"
    # Counter for different titles and users
    num = 0
    # Goes through each line
    for line in text:
        start_date = line.strip()
        # Creates and registers a user for each line
        user_email = "otheruseragain" + str(num) + "@gmail.com"
        register("otheruseragain" + str(num), user_email, "Abc12!")
        # Creates a listing
        temp_title = title + str(num)
        create_listing(temp_title, "A very valid description.", 800,
                       "2022-11-11", "owner3@gmail.com")
        # Test to see if it creates the booking
        # (with a different listing each time)
        try:
            create_booking(user_email, temp_title, start_date, "2022-11-13")
        except Exception():
            print("An error occurred")
        num += 1
    file1.close()


def test_end_date_create_booking():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers an owner
    register("owner4", "owner4@gmail.com", "Abc12!")
    title = "CoolTitle#"
    # Counter for different titles and users
    num = 0
    # Goes through each line
    for line in text:
        end_date = line.strip()
        # Creates and registers a user for each line
        user_email = "anotheruseragain" + str(num) + "@gmail.com"
        register("anotheruseragain" + str(num), user_email, "Abc12!")
        # Creates a listing
        temp_title = title + str(num)
        create_listing(temp_title, "A very valid description.", 800,
                       "2022-11-11", "owner4@gmail.com")
        # Test to see if it creates the booking
        # (with a different listing each time)
        try:
            create_booking(user_email, temp_title, "2022-11-13", end_date)
        except Exception():
            print("An error occurred")
        num += 1
    file1.close()