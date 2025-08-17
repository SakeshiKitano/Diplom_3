import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as L
from locators.details_window_locators import ModalLocators as M
from locators.order_feed_locators import FeedPageLocators as F
from locators.header_locators import HeaderLocators as H
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    @allure.step("Дождаться загрузкм главной страницы")
    def main_page_loading_wait(self, timeout=10):
        self.wait_for_element (L.TITLE_CONSTRUCTOR)


    @allure.step("Нажать на 'Конструктор' в хедере")
    def go_to_constructor(self):
        self.click_on_element(H.CONSTRUCTOR_BTN)

    @allure.step("Нажать на 'Лента заказов' в хедере")
    def go_to_feed(self):
        self.click_with_js(H.FEED_BTN)

    @allure.step("Скролл до элемента из конструктора")
    def scroll_to_ingredient(self, name):
        self.scroll_to_element(L.INGREDIENT_CARD_BY_NAME(name), timeout=10)

    @allure.step("Открыть модал ингредиента по имени: {name}")
    def open_ingredient_modal(self, name):
        locator = L.INGREDIENT_CARD_BY_NAME(name)
        element = self.wait_for_clickable(locator)  # ждем, пока элемент станет кликабельным
        try:
            element.click()
        except:
            # fallback через JS
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_modal(self):
        self.click_on_element(M.CLOSE_BTN)

    @allure.step("Ожидание закрытия модального окна")
    def wait_modal_closed(self, timeout=5):
        try:
            self.wait_for_no_element(M.MODAL_ROOT, timeout)
            return True
        except TimeoutException:
            return False

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



    @allure.step('Перетащить элемент в корзину')
    def put_ingredient_into_basket(self, name):
        #self.main_page_loading_wait()
        ingredient = self.find_element_with_wait(locator=L.INGREDIENT_CARD_BY_NAME(name))
        basket = self.find_element_with_wait(locator=L.CONSTRUCTOR_DROP_AREA)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Ожидать модальное окно ингредиента")
    def wait_modal_visible(self):
        return self.find_element_with_wait(M.MODAL_ROOT)

    @allure.step("Получить текст заголовка Соберите бургер")
    def get_text_konstrukt_tittle(self):
        self.wait_for_element(L.TITLE_CONSTRUCTOR)
        return self.get_text_on_element(L.TITLE_CONSTRUCTOR)

    @allure.step("Получить текст заголовка окна с ингридиентами")
    def get_text_modal_tittle(self):
        self.wait_for_element(M.MODAL_TITLE)
        return self.get_text_on_element(M.MODAL_TITLE)

    @allure.step("Нажать на кнопку Заказать")
    def click_place_an_order(self):
        self.click_on_element(L.PLACE_AN_ORDER)

    @allure.step("Дождаться и получить Id заказа")
    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(M.ORDER_ID, "9999")
        return self.get_text_on_element(M.ORDER_ID)

    @allure.step("Закрыть окно с деталями заказа")
    def click_close_order_details(self):
        self.wait_for_element(M.CLOSE_ORDER_DETAILS_BUTTON)
        self.click_on_element(M.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step("Получить текст заголовка окна деталей заказа")
    def get_text_order_tittle(self):
        self.wait_for_element(M.ORDER_TITLE)
        return self.get_text_on_element(M.ORDER_TITLE)

    @allure.step("Дождаться закрытия оверлея Id заказа")
    def get_invisiblity_id_order_overlay(self):
        self.wait_for_no_element(M.ORDER_ID_OVERLAY_LOCATOR)

    @allure.step("Получить текст заголовка окна деталей заказа")
    def get_click_id_order_overlay(self):
        self.click_on_element(M.ORDER_ID_OVERLAY_LOCATOR)



