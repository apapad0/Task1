from login_test1_space_after_email import test as test1
from login_test2_spaces_in_the_email_field import test as test2
from login_test3_empty_email_field import test as test3
from login_test4_empty_password_field import test as test4
from login_test5_both_fields_empty import test as test5


TESTS = [test1, test2, test3, test4, test5]

if __name__ == "__main__":
    for test in TESTS:
        if test():
            print("Test", TESTS.index(test) + 1, ": PASS")
        else:
            print("Test", TESTS.index(test) + 1, ": FAIL")
