"""Locators for tests. Locators of the same page/window belong to same class."""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """The class for main page locators: http://mail.ru ."""
    LOGIN = (By.XPATH, './/input[@id="mailbox:login"]')
    DOMAIN_MAIL = (By.XPATH, './/select[@id="mailbox:domain"]/option[text()="@mail.ru"]')
    AUTH_BUTTON = (By.XPATH, './/label[@id="mailbox:submit"]/input[@class="o-control"]')
    PASSWD = (By.XPATH, './/input[@id="mailbox:password"]')
    ERROR = (By.XPATH, './/div[@id="mailbox:error"]')


class InboxPageLocators:
    """The class for inbox page locators: https://e.mail.ru/inbox/ ."""
    COMPOSE_BUTTON = (By.XPATH, './/div[starts-with(@class, "sidebar__compose-btn-box")]/a')


class ComposeWindowLocators:
    """The class for compose window locators."""
    COMPOSE_WINDOW = (By.XPATH, './/div[@class="compose-app__widgets"]')
    MSG_TO = (By.XPATH, './/div[@class="contacts--1ofjA"]/descendant::input')
    MSG_SUBJECT = (By.XPATH, './/input[@name="Subject"]')
    MSG_TEXT = (By.XPATH, './/div[starts-with(@class, "editable-container")]/div/div')
    SEND_BUTTON = (By.XPATH, './/span[@title="Send"]')


class SentWindowLocators:
    """The class for sent window locators."""
    SENT_WINDOW = (By.XPATH, './/div[@class="layer-sent-page__controls"]')
    SENT_STATUS = (By.XPATH, './/a[@class="layer__link"]')
