
from .pages.calculator_page import CalculatorPage
from .pages.home_page import HomePage

def test_calculator_with_integers(browser):
    link = f"http://google.com/"
    page = HomePage(browser, link)
    page.open()
    page.go_to_calculator_page()
    calculator_page = CalculatorPage(browser, browser.current_url)
    calculator_page.checking_operations_with_integers()

def test_calculator_with_zero(browser):
    link = f"http://google.com/"
    page = HomePage(browser, link)
    page.open()
    page.go_to_calculator_page()
    calculator_page = CalculatorPage(browser, browser.current_url)
    calculator_page.checking_division_by_zero()

def test_calculator_with_missing_values(browser):
    link = f"http://google.com/"
    page = HomePage(browser, link)
    page.open()
    page.go_to_calculator_page()
    calculator_page = CalculatorPage(browser, browser.current_url)
    calculator_page.checking_error_if_missing_values()