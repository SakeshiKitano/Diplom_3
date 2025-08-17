import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from data import *


@allure.title('Тест увеличения общего счётчика заказов')
def test_total_orders_counter_increases_after_new_order(driver):
    feed_page = FeedPage(driver)
    main_page = MainPage(driver)
    account_page = LoginPage(driver)

    with allure.step('Выполняем вход в аккаунт'):
        account_page.login(EMAIL, PASSWORD)
        main_page.get_text_konstrukt_tittle()
    with allure.step('Открываем ленту заказов'):
        main_page.go_to_feed()

    with allure.step('Получаем начальный счётчик заказов'):
        initial_total_orders = feed_page.get_total_orders()

    with allure.step('Создаем новый заказ'):
        feed_page.go_to_constructor()

        main_page.put_ingredient_into_basket(FIRST_INGREDIENT)
        main_page.click_place_an_order()

        main_page.get_order_id_from_details()
        main_page.get_text_order_tittle()
        main_page.click_close_order_details()

    with allure.step('Проверяем, что общий счётчик заказов увеличился'):
        main_page.go_to_feed()
        updated_total_orders = feed_page.get_total_orders()
        assert updated_total_orders > initial_total_orders, \
            f"Ожидалось увеличение счетчика. Было: {initial_total_orders}, стало: {updated_total_orders}"

@allure.title('Тест увеличения счётчика заказов за сегодня')
def test_today_orders_counter_increases_after_new_order(driver):
    feed_page = FeedPage(driver)
    main_page = MainPage(driver)
    account_page = LoginPage(driver)

    with allure.step('Выполняем вход в аккаунт'):
        account_page.login(EMAIL, PASSWORD)
        main_page.get_text_konstrukt_tittle()
    with allure.step('Открываем ленту заказов'):
        main_page.go_to_feed()

    with allure.step('Получаем начальный счётчик заказов'):
        initial_today_orders = feed_page.get_today_orders()

    with allure.step('Создаем новый заказ'):
        feed_page.go_to_constructor()

        main_page.put_ingredient_into_basket(FIRST_INGREDIENT)
        main_page.click_place_an_order()

        main_page.get_order_id_from_details()
        main_page.get_text_order_tittle()
        main_page.click_close_order_details()

    with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
        main_page.go_to_feed()
        updated_today_orders = feed_page.get_today_orders()
        assert updated_today_orders > initial_today_orders, \
            f"Ожидалось увеличение счетчика. Было: {initial_today_orders}, стало: {updated_today_orders}"


@allure.title('Тест отображения номера заказа в разделе "В работе"')
def test_order_number_appears_in_in_progress_after_order_placement(driver):

    feed_page = FeedPage(driver)
    main_page = MainPage(driver)
    account_page = LoginPage(driver)

    with allure.step('Выполняем вход в аккаунт'):
        account_page.login(EMAIL, PASSWORD)

    with allure.step('Создаем новый заказ'):
        main_page.main_page_loading_wait()
        main_page.put_ingredient_into_basket(FIRST_INGREDIENT)
        main_page.click_place_an_order()

    with allure.step('Получаем идентификатор заказа'):
        order_id = main_page.get_order_id_from_details()

    with allure.step('Закрываем модальное окно и проверяем раздел "В работе"'):
        main_page.click_close_order_details()
        main_page.go_to_feed()

    with allure.step('Проверяем, что номер заказа появился в разделе "В работе"'):
        assert feed_page.is_order_number_in_progress(order_id), \
            f"Номер заказа {order_id} не появился в разделе 'В работе'"