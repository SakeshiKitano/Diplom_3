from selenium.webdriver.common.by import By

class HeaderLocators:
    # ==== Хедер ====
    CONSTRUCTOR_BTN = (By.XPATH, "//p[normalize-space()='Конструктор']")  # Кнопка "Конструктор" в верхнем меню
    FEED_BTN = (By.XPATH, "//p[normalize-space()='Лента Заказов']")  # Кнопка "Лента заказов" в верхнем меню
    CABINET_BTN = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")  # Кнопка "Личный кабинет" в верхнем меню