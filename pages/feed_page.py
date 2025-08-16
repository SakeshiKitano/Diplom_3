import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as L
from locators.details_window_locators import ModalLocators as M
from locators.order_feed_locators import FeedPageLocators as F
from locators.header_locators import HeaderLocators as H

class FeedPage(BasePage):

    @allure.step("Получить текст заголовка Лента заказов")
    def get_text_feeder_tittle(self):
        self.wait_for_element(F.FEED_TITLE)
        return self.get_text_on_element(F.FEED_TITLE)

    @allure.step("Нажать на 'Конструктор' в хедере")
    def go_to_constructor(self):
        self.click_on_element(H.CONSTRUCTOR_BTN)