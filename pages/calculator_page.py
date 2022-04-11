from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import CalculatorPageLocators


class CalculatorPage(BasePage):

    def checking_operations_with_integers(self):
        input = self.browser.find_element(*CalculatorPageLocators.INPUT_FIELD)
        input.send_keys("(1 + 2) × 3 - 40 / 5")
        input.send_keys(Keys.RETURN)
        assert self.browser.find_element(*CalculatorPageLocators.HISTORY_FIELD).text == "(1 + 2) × 3 - 40 ÷ 5 =", \
            "Неверное значение в строке памяти"
        assert self.browser.find_element(*CalculatorPageLocators.RESULT_FIELD).text == "1", \
            "Неверное значение в строке результата"

    def checking_division_by_zero(self):
        input = self.browser.find_element(*CalculatorPageLocators.INPUT_FIELD)
        input.send_keys("6 / 0")
        input.send_keys(Keys.RETURN)
        assert self.browser.find_element(*CalculatorPageLocators.HISTORY_FIELD).text == "6 ÷ 0 =", \
            "Неверное значение в строке памяти"
        assert self.browser.find_element(*CalculatorPageLocators.RESULT_FIELD).text == "Infinity", \
            "Неверное значение в строке результата"

    def checking_error_if_missing_values(self):
        input = self.browser.find_element(*CalculatorPageLocators.INPUT_FIELD)
        input.send_keys("sin")
        input.send_keys(Keys.RETURN)
        assert self.browser.find_element(*CalculatorPageLocators.HISTORY_FIELD).text == "sin() =", \
            "Неверное значение в строке памяти"
        assert self.browser.find_element(*CalculatorPageLocators.RESULT_FIELD).text == "Error", \
            "Неверное значение в строке результата"