from selenium.webdriver.common.by import By

class FeedPageLocators:
    # ==== Хедер ====
    HEADER_FEED_LINK = (By.XPATH, "//p[normalize-space()='Лента Заказов']")  # Кнопка "Лента заказов" в верхнем меню

    FEED_TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']") # Заголовок лента заказов

    # ==== Счетчики ====
    COUNTER_TOTAL_LABEL = (By.XPATH, "//p[normalize-space()='Выполнено за все время:']")  # Лейбл "Выполнено за все время"
    COUNTER_TODAY_LABEL = (By.XPATH, "//p[normalize-space()='Выполнено за сегодня:']")  # Лейбл "Выполнено за сегодня"
    COUNTER_TOTAL_VALUE = (By.XPATH, "//p[normalize-space()='Выполнено за все время:']/following-sibling::p[1]")  # Значение счетчика "Выполнено за все время"
    COUNTER_TODAY_VALUE = (By.XPATH, "//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p[1]")  # Значение счетчика "Выполнено за сегодня"

    # ==== Колонка "В работе" ====
    COLUMN_IN_PROGRESS_NUMBERS = (By.XPATH, "//h2[contains(., 'В работе')]/following-sibling::ul[1]/li")
    # Список номеров заказов в колонке "В работе"
