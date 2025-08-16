import allure
import pytest

from curl import order_feed_page, main_site
from pages.main_page import MainPage
from pages.feed_page import FeedPage

INGREDIENT_NAME = "Флюоресцентная булка R2-D3"

@allure.feature("Навигация")
@allure.story("Переход из 'Ленты заказов' обратно на 'Конструктор'")
def test_navigation_feed_to_constructor(driver):
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
@allure.story("Переход по клику на 'Лента заказов'")
def test_feed_navigation(driver):
    page = MainPage(driver)
    with allure.step("Кликнуть 'Лента заказов'"):
        page.go_to_feed()
    page = FeedPage(driver)
    with allure.step("Проверить, что мы на странице Лента заказов"):
        title = page.get_text_feeder_tittle()
        assert title == "Лента заказов"
        assert driver.current_url == order_feed_page
