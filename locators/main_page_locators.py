from selenium.webdriver.common.by import By

class MainPageLocators:

    # ==== Заголовок конструктора ====
    TITLE_CONSTRUCTOR = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")  # Заголовок главной страницы конструктора

    # ==== Ингредиенты ====
    INGREDIENT_CARD_BY_NAME = lambda name: (
    By.XPATH,
    f"//p[normalize-space()='{name}']/ancestor::a[contains(@class,'BurgerIngredient_ingredient')]"
) # Карточка ингредиента по имени (например: "Флюоресцентная булка R2-D3")

    INGREDIENT_COUNTER_BY_NAME = lambda name: (
        By.XPATH,
        f"//p[normalize-space()='{name}']/ancestor::*[self::a or self::div]"
        f"//*[contains(@class,'counter') and contains(@class,'num')]"
    ) # Счетчик количества для ингредиента (появляется при добавлении в заказ)

    # ==== Зона конструктора ====
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    # Область, куда перетаскиваются ингредиенты для сборки бургера

    # ==== Табы категорий ====
    TAB_BUNS = (By.XPATH, "//span[normalize-space()='Булки']/parent::div[contains(@class,'tab')]") # Вкладка "Булки"
    TAB_SAUCES = (By.XPATH, "//span[normalize-space()='Соусы']/parent::div[contains(@class,'tab')]") # Вкладка "Соусы"
    TAB_FILLINGS = (By.XPATH, "//span[normalize-space()='Начинки']/parent::div[contains(@class,'tab')]") # Вкладка "Начинки"


