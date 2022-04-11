from selenium.webdriver.common.keys import Keys

from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):

    def go_to_calculator_page(self):
        input = self.browser.find_element(*HomePageLocators.INPUT_FIELD)
        input.send_keys("Калькулятор")
        input.send_keys(Keys.RETURN)