from qbnb.models import register
from qbnb.models import create_listing
import random
import string


def test_title_create_listing():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers a user
    register("bengo3", "bengo3@gmail.com", "Abc12!")
    # Counter for different titles
    title_num = 0
    # Go through each line
    for line in text:
        title = line.strip()
        title_num += 1
        temp_title = title + str(title_num)
        # Tests the title for create listing (different title each time)
        try:
            create_listing(temp_title, "A very valid description.",
                           800, "2022-11-11", "bengo3@gmail.com")
        except Exception():
            print("An error occurred")
    file1.close()


def test_desc_create_listing():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers a user
    register("bengo0", "bengo0@gmail.com", "Abc12!")
    # Initialize a title
    title = "BestTitle#"
    # Counter for different titles
    title_num = 0
    # Go through each line
    for line in text:
        desc = line.strip()
        title_num += 1
        # Different title each time
        temp_title = title + str(title_num)
        # Tests the description for create listing
        # (with a different title each time)
        try:
            create_listing(temp_title, desc, 800, "2022-11-11",
                           "bengo0@gmail.com")
        except Exception():
            print("An error occurred")
    file1.close()


def test_price_create_listing():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()
    # Creates and registers a user
    register("bengo22", "bengo22@gmail.com", "Abc12!")
    # Initialize a title
    title = "BestTitle#"
    # Counter for different titles
    title_num = 0
    # Go through each line
    for line in text:
        price = line.strip()
        title_num += 1
        # Different title each time
        temp_title = title + str(title_num)
        # Tests the price for create listing
        # (with a different title each time)
        try:
            create_listing(temp_title, "A very valid description.",
                           price, "2022-11-11", "bengo22@gmail.com")
        except Exception():
            print("An error occurred")
    file1.close()