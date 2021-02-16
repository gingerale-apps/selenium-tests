"""Creating an object with action methods for each web page."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from locators import MainPageLocators, InboxPageLocators, ComposeWindowLocators, SentWindowLocators


class BasePage:
    """
    Base class to initialize the base page that will be called from all pages.
    Also contains common methods for pages.
    """
    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator, method=ec.visibility_of_element_located, time=10):
        """This is used by pages methods to change parameters wait of elements."""
        return WebDriverWait(self.driver, time).until(method(locator), message=f"Can't find element: {locator}")

    def check_window_loaded(self, final_element):
        """This is used by pages methods to determines if the last DOM element of the window is loaded."""
        try:
            return self.wait_element(final_element)
        except TimeoutException:
            return False


class MainPage(BasePage):
    """Main page action methods: http://mail.ru ."""

    def login(self, user, passwd):
        """Inserts email, domain, password to form and clicks auth button."""
        self.driver.find_element(*MainPageLocators.LOGIN).send_keys(user)
        self.driver.find_element(*MainPageLocators.DOMAIN_MAIL).click()
        self.driver.find_element(*MainPageLocators.AUTH_BUTTON).click()
        self.wait_element(MainPageLocators.PASSWD).send_keys(passwd)
        self.driver.find_element(*MainPageLocators.AUTH_BUTTON).click()

    def is_login_success(self):
        """
        Determines if user is signed in. Returns True if main page redirects to inbox page, else returns error text.
        """
        try:
            return self.wait_element('https://e.mail.ru/inbox/', method=ec.url_contains, time=15)
        except TimeoutException:
            return self.wait_element(MainPageLocators.ERROR).text


class InboxPage(BasePage):
    """Inbox page action methods: https://e.mail.ru/inbox/ ."""

    def click_compose_button(self):
        """Clicks compose button."""
        self.wait_element(InboxPageLocators.COMPOSE_BUTTON).click()


class ComposeWindow(BasePage):
    """Action methods for compose window."""

    def is_compose_window_loaded(self):
        """Checks visibility of last DOM element in compose window."""
        return self.check_window_loaded(ComposeWindowLocators.COMPOSE_WINDOW)

    def create_and_send_message(self, to_user, subject, text):
        """Inserts to, subject, text to compose window and clicks send button."""
        self.driver.find_element(*ComposeWindowLocators.MSG_TO).send_keys(to_user)
        self.driver.find_element(*ComposeWindowLocators.MSG_SUBJECT).send_keys(subject)
        self.driver.find_element(*ComposeWindowLocators.MSG_TEXT).send_keys(text)
        self.driver.find_element(*ComposeWindowLocators.SEND_BUTTON).click()


class SentWindow(BasePage):
    """Action methods for sent window."""

    def is_sent_window_loaded(self):
        """Checks visibility of last DOM element in sent window."""
        return self.check_window_loaded(SentWindowLocators.SENT_WINDOW)

    def is_msg_sent(self):
        """Checks if message sent."""
        return self.driver.find_element(*SentWindowLocators.SENT_STATUS).text == 'Message sent'
