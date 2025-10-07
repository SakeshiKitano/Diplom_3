from selenium.webdriver.common.by import By

class ModalLocators:
    MODAL_ROOT = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    # Само модальное окно

    MODAL_TITLE = (By.XPATH, "//h2[contains(@class,'text_type_main-large') or contains(., 'Детали ингредиента')]")
    # Заголовок внутри модалки ("Детали ингредиента")

    CLOSE_BTN = (By.XPATH, "//button[contains(@class,'Modal_modal__close') or @aria-label='Закрыть']")
    # Крестик закрытия модального окна

    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")
    #Id заказа

    CLOSE_ORDER_DETAILS_BUTTON = (By.XPATH, "//button[@type='button']//*[name()='svg']")
    #Кнопка закрыть окно с Id заказа

    ORDER_TITLE = (By.XPATH,
                          "//section[contains(@class,'Modal_modal_opened')]" \
                  "//div[contains(@class,'Modal_modal__contentBox')]" \
                  "//p[contains(@class,'text_type_main-medium') and contains(@class,'mb-15')]")

    ORDER_ID_OVERLAY_LOCATOR = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
