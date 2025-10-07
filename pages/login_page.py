import allure

from curl import login_url
from .base_page import BasePage
from locators.login_page_locators import AccountPageLocators as A


class LoginPage(BasePage):

    @allure.step("Перемещение на страницу логина")
    def open_login_page(self):
        self.navigate_to(login_url)

    @allure.step("Ввести данные логина и нажать кнопку регистрации")
    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(A.EMAIL_INPUT, email)
        self.add_text_to_element(A.PASSWORD_INPUT, password)
        self.click_with_js(A.LOGIN_BUTTON)