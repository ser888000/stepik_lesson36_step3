from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

class TestButton:
    def test_button(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
#        time.sleep(30)
        assert button, 'Button not found' # бесполезная строка, так если тест падает, то до нее дело не доходит

