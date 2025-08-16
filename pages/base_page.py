import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельность элемента")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_clickable(locator, timeout)
        element.click()


    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step("Ожидание появления элемента {locator}")
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, source_locator, target_locator):

        element_from = self.find_element_with_wait(source_locator)
        element_to = self.find_element_with_wait(target_locator)

        try:
            # Попытка через ActionChains
            actions = ActionChains(self.driver)
            actions.drag_and_drop(element_from, element_to).perform()
        except WebDriverException:
            # Если не сработало (обычно на React), пробуем через JS
            self.driver.execute_script("""
                function triggerDragAndDrop(src, dst) {
                    const dataTransfer = new DataTransfer();

                    const dragStartEvent = new DragEvent('dragstart', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    src.dispatchEvent(dragStartEvent);

                    const dragEnterEvent = new DragEvent('dragenter', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    dst.dispatchEvent(dragEnterEvent);

                    const dragOverEvent = new DragEvent('dragover', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    dst.dispatchEvent(dragOverEvent);

                    const dropEvent = new DragEvent('drop', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    dst.dispatchEvent(dropEvent);

                    const dragEndEvent = new DragEvent('dragend', {
                        bubbles: true,
                        cancelable: true,
                        dataTransfer: dataTransfer
                    });
                    src.dispatchEvent(dragEndEvent);
                }
                triggerDragAndDrop(arguments[0], arguments[1]);
            """, element_from, element_to)
