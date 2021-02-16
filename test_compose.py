"""
Test for mail.ru.
Python 3.7, selenium and page object pattern are used.

Check chromedriver version before start:
(download: https://sites.google.com/a/chromium.org/chromedriver/downloads)
"""

import os
import unittest
from selenium import webdriver
import pages


class EmailSendingTest(unittest.TestCase):
    """Checks email sending."""
    def setUp(self):
        self.driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
        self.driver.get('https://mail.ru/')

    def tearDown(self):
        self.driver.close()

    def test_login_compose(self):
        """
        Test actions:
        - login on main page https://mail.ru/
        - open compose window
        - compose and send email
        - check sending email
        """
        main_page = pages.MainPage(self.driver)
        main_page.login('mouse17_89', 'pass')
        auth_result = main_page.is_login_success()
        assert auth_result is True, f'Authorization failed. Error: {auth_result}.'

        inbox_page = pages.InboxPage(self.driver)
        inbox_page.click_compose_button()

        compose_window = pages.ComposeWindow(self.driver)
        assert compose_window.is_compose_window_loaded(), "Compose window is not loaded."
        compose_window.create_and_send_message('mouse17_89@mail.ru', 'test message', 'Hello!')

        sent_window = pages.SentWindow(self.driver)
        assert sent_window.is_sent_window_loaded(), "Sent window is not loaded."
        assert sent_window.is_msg_sent(), "Message is not sent."


if __name__ == "__main__":
    unittest.main()
