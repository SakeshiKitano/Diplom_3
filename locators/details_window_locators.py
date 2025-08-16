from selenium.webdriver.common.by import By

class ModalLocators:
    MODAL_ROOT = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    # Само модальное окно

    MODAL_TITLE = (By.XPATH, "//h2[contains(@class,'text_type_main-large') or contains(., 'Детали ингредиента')]")
    # Заголовок внутри модалки ("Детали ингредиента")

    CLOSE_BTN = (By.XPATH, "//button[contains(@class,'Modal_modal__close') or @aria-label='Закрыть']")
    # Крестик закрытия модального окна
