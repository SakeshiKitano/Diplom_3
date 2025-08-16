import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as L
from locators.details_window_locators import ModalLocators as M
from locators.order_feed_locators import FeedPageLocators as F
from locators.header_locators import HeaderLocators as H

class MainPage(BasePage):
    @allure.step("Нажать на 'Конструктор' в хедере")
    def go_to_constructor(self):
        self.click_on_element(H.CONSTRUCTOR_BTN)

    @allure.step("Нажать на 'Лента заказов' в хедере")
    def go_to_feed(self):
        self.click_on_element(H.FEED_BTN)

    @allure.step("Открыть модал ингредиента по имени: {name}")
    def open_ingredient_modal(self, name):
        self.click_on_element(L.INGREDIENT_CARD_BY_NAME(name))

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click_on_element(M.CLOSE_BTN)

    @allure.step("Получить значение счетчика ингредиента по имени: {name}")
    def get_ingredient_counter(self, name):
        try:
            text = self.get_text_on_element(L.INGREDIENT_COUNTER_BY_NAME(name))
        except (TimeoutException, NoSuchElementException):
            return 0
        try:
            return int(text)
        except Exception:
            return 0

    @allure.step("Добавить ингредиент в заказ (drag&drop): {name}")
    def add_ingredient_to_constructor(self, name):
        self.drag_and_drop(L.INGREDIENT_CARD_BY_NAME(name), L.CONSTRUCTOR_DROP_AREA)

    @allure.step("Ожидать модальное окно ингредиента")
    def wait_modal_visible(self):
        return self.find_element_with_wait(M.MODAL_ROOT)

    @allure.step("Получить текст заголовка Соберите бургер")
    def get_text_konstrukt_tittle(self):
        self.wait_for_element(L.TITLE_CONSTRUCTOR)
        return self.get_text_on_element(L.TITLE_CONSTRUCTOR)

