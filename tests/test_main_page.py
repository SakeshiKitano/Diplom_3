import allure

from curl import order_feed_page, main_site
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from data import *

class TestMainPage:

    @allure.title("Переход из 'Ленты заказов' обратно на 'Конструктор'")
    def test_navigation_feed_to_constructor(self, driver):
        page = MainPage(driver)
        with allure.step("Перейти в 'Ленту заказов'"):
            page.go_to_feed()
        page = FeedPage(driver)
        with allure.step("Проверить, что мы на странице Лента заказов"):
            title = page.get_text_feeder_tittle()
            assert title == "Лента заказов"
            assert driver.current_url == order_feed_page
        with allure.step("Перейти обратно в 'Конструктор'"):
            page.go_to_constructor()
        page = MainPage(driver)
        with allure.step("Проверить, что мы на главной странице"):
            title = page.get_text_konstrukt_tittle()
            assert title == 'Соберите бургер'
            assert driver.current_url == main_site


    @allure.feature("Навигация")
    @allure.title("Переход по клику на 'Лента заказов'")
    def test_feed_navigation(self,driver):
        page = MainPage(driver)
        with allure.step("Кликнуть 'Лента заказов'"):
            page.go_to_feed()
        page = FeedPage(driver)
        with allure.step("Проверить, что мы на странице Лента заказов"):
            title = page.get_text_feeder_tittle()
            assert title == "Лента заказов"
            assert driver.current_url == order_feed_page

    @allure.feature("Модальное окно ингредиента")
    @allure.title("Открытие")
    def test_ingredient_modal_open(self, driver):
        page = MainPage(driver)
        with allure.step(f"Открыть модал ингредиента '{INGREDIENT_NAME}'"):
            page.scroll_to_ingredient(INGREDIENT_NAME)
            page.open_ingredient_modal(INGREDIENT_NAME)
            page.wait_modal_visible()
        with allure.step("Проверка что окно открылось"):
            tittle = page.get_text_modal_tittle()
            assert tittle == 'Детали ингредиента'

    @allure.feature("Модальное окно ингредиента")
    @allure.title("Закрытие модалки ингредиента")
    def test_ingredient_modal_close(self, driver):
        page = MainPage(driver)
        with allure.step(f"Открыть модал ингредиента '{INGREDIENT_NAME}'"):
            page.scroll_to_ingredient(INGREDIENT_NAME)
            page.open_ingredient_modal(INGREDIENT_NAME)
            page.wait_modal_visible()
        with allure.step("Проверка что окно открылось"):
            tittle = page.get_text_modal_tittle()
            assert tittle == 'Детали ингредиента'
        page.close_modal()
        with allure.step("Проверка что окно закрылось"):
            assert page.wait_modal_closed()

    @allure.feature("Конструктор")
    @allure.title("Счетчик ингредиента увеличивается после добавления в заказ")
    def test_counter_increases_after_add(self, driver):
        page = MainPage(driver)
        with allure.step(f"Считать текущее значение счетчика для '{FIRST_INGREDIENT}'"):
            before = page.get_ingredient_counter(FIRST_INGREDIENT)
        with allure.step("Добавить ингредиент в конструктор"):
            page.put_ingredient_into_basket(FIRST_INGREDIENT)
        with allure.step("Проверить, что счетчик увеличился"):
            after = page.get_ingredient_counter(FIRST_INGREDIENT)
            assert after > before, f"Ожидали увеличение счетчика: было {before}, стало {after}"