import allure

from .base_page import BasePage
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

    @allure.step("Получить 'Выполнено за все время'")
    def get_total_orders(self):
        self.wait_for_element(F.COUNTER_TOTAL_VALUE)
        return int(self.get_text_on_element(F.COUNTER_TOTAL_VALUE).replace(' ', ''))


    @allure.step("Получить 'Выполнено за сегодня'")
    def get_today_orders(self):
        self.wait_for_element(F.COUNTER_TODAY_VALUE)
        return int(self.get_text_on_element(F.COUNTER_TODAY_VALUE).replace(' ', ''))

    @allure.step("Проверка отображения номера заказа в разделе 'В работе'")
    def is_order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Форматирование с ведущими нулями
        self.find_and_format_locator(F.COLUMN_IN_PROGRESS_NUMBERS, formatted_id)
        return True