import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as L

class MainPage(BasePage):
    @allure.step("Нажать на 'Конструктор' в хедере")
    def go_to_constructor(self):
        self.click(L.CONSTRUCTOR_BTN)

    @allure.step("Нажать на 'Лента заказов' в хедере")
    def go_to_feed(self):
        self.click(L.FEED_BTN)

    @allure.step("Открыть модал ингредиента по имени: {name}")
    def open_ingredient_modal(self, name):
        self.click(L.INGREDIENT_CARD_BY_NAME(name))

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click(L.MODAL_CLOSE)

    @allure.step("Получить значение счетчика ингредиента по имени: {name}")
    def get_ingredient_counter(self, name):
        try:
            text = self.get_text(L.INGREDIENT_COUNTER_BY_NAME(name))
        except (TimeoutException, NoSuchElementException):
            return 0
        try:
            return int(text)
        except Exception:
            return 0

    @allure.step("Добавить ингредиент в заказ (drag&drop): {name}")
    def add_ingredient_to_constructor(self, name):
        self.drag_and_drop_html5(L.INGREDIENT_CARD_BY_NAME(name), L.CONSTRUCTOR_DROP_AREA)

    @allure.step("Ожидать модальное окно ингредиента")
    def wait_modal_visible(self):
        return self.is_visible(L.MODAL)
