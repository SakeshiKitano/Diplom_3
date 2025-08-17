import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from curl import login_url
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as L
from locators.details_window_locators import ModalLocators as M
from locators.order_feed_locators import FeedPageLocators as F
from locators.header_locators import HeaderLocators as H
from locators.login_page_locators import AccountPageLocators as A
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    def open_login_page(self):
        self.navigate_to(login_url)

    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(A.EMAIL_INPUT, email)
        self.add_text_to_element(A.PASSWORD_INPUT, password)
        self.click_with_js(A.LOGIN_BUTTON)