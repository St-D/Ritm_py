#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

from base_app import BasePage
from selenium.webdriver.common.by import By


class DemoQaIndexPageLocators:
    LOCATOR_ELEMENTS_ICON = (By.XPATH, "//h5[text()='Elements']")


class IndexPage(BasePage):

    def click_on_the_elements_icon(self):
        return self.find_element(DemoQaIndexPageLocators.LOCATOR_ELEMENTS_ICON, time=10).click()
