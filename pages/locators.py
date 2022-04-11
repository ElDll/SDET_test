from selenium.webdriver.common.by import By

class BasePageLocators():
    FUCK_BUTTON = (By.XPATH, "//div[@class='QS5gu sy4vM']/button")

class HomePageLocators():
    INPUT_FIELD = (By.CLASS_NAME, "gLFyf")

class CalculatorPageLocators():
    INPUT_FIELD = (By.CLASS_NAME, "jlkklc")
    HISTORY_FIELD = (By.CLASS_NAME, "vUGUtc")
    RESULT_FIELD = (By.CLASS_NAME, "qv3Wpe")