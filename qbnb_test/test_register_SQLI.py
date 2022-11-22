from qbnb.models import register
import random
import string


def test_user_register():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()

    email = "steve@steve.com"
    user_num = 0

    for line in text:
        user = line.strip()
        user_num += 1
        temp_email = str(user_num) + email

        try:
            register(user, temp_email, "Abc12!")
        except Exception():
            print("An error occurred")

    file1.close()


def test_email_register():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()

    username = "jerry1"
    user_num = 0

    for line in text:
        email = line.strip()
        user_num += 1
        temp_username = username + str(user_num)

        try:
            register(temp_username, email, "Abc12!")
        except Exception():
            print("An error occurred")

    file1.close()


def test_password_register():
    file1 = open('qbnb_test/Generic_SQLI.txt', 'r')
    text = file1.readlines()

    email = "buckey@bob0.com"
    username = "buckey"
    user_num = 0

    for line in text:
        password = line.strip()
        user_num += 1
        temp_username = str(user_num) + username
        temp_email = str(user_num) + email

        try:
            register("test1", "test44@test44.com", password)
        except Exception():
            print("An error occurred")

    file1.close()