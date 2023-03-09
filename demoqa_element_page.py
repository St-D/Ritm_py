#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

from base_app import BasePage
from selenium.webdriver.common.by import By


class DemoQaElementsPageLocators:
    LOCATOR_CHECKBOX_ICON = (By.XPATH, "//span[text()='Check Box']")


class ElementPage(BasePage):

    def click_on_the_check_box_icon(self):
        return self.find_element(DemoQaElementsPageLocators.LOCATOR_CHECKBOX_ICON, time=10).click()
