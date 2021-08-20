# Task1: Create test cases and scenarios for an existing application.

This project runs as a supplementary test to the *Login* freature of https://app.omicsanalytics.com/login.

**Instructions**

1. git clone https://github.com/msRob0t/Task1
2. pip install -r requirements.txt
3. Enter credentials in config.py
4. python main.py

We examine 5 test cases:
- test1: space after email
- test2: spaces in the email field
- test3: empty email field
- test4: empty password field
- test5: both fields empty

**Reminder:** To run the code successfully it's crucial to fill the config.py file with the right email and password.

**Note 1:**  All tests were written to return 'PASS' when the test *fails successfully*. 

**Note 2:**  Test1 had a different reaction when tested manually and concidernig the manual test as the correct one test1 should fail. 
