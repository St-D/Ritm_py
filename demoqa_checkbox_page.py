#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

from base_app import BasePage
from selenium.webdriver.common.by import By


class DemoQaCheckBoxPageLocators:
    LOCATOR_ROOT_CHECKBOX_TREE_BUTTON = (By.XPATH, "//button[@title='Toggle']")
    LOCATOR_OTHER_DIR = (By.XPATH, "//span[@class='rct-title']")
    LOCATOR_DOWNLOADS_DIR_CHECKBOX_BUTTON = (By.XPATH, "(//button[@title='Toggle'])[4]")
    LOCATOR_FILES_IN_DOWNLOADS = (By.XPATH, "//span[@class='rct-title' and contains(text(),'.doc')]")
    LOCATOR_SELECT_FILE_IN_DOWNLOADS = (By.XPATH, "//span[@class='rct-title' and text()='Word File.doc']")
    LOCATOR_CHECK_SELECTED_FILE = (By.XPATH, "//div[@id='result']/span")


class CheckBoxPage(BasePage):

    def click_on_the_root_check_box_tree_button(self):
        return self.find_element(DemoQaCheckBoxPageLocators.LOCATOR_ROOT_CHECKBOX_TREE_BUTTON, time=10).click()

    def find_tree_elements(self, lctr):
        another_dir_list = self.find_elements(lctr, time=10)
        print('\n\n Has found ' + str(len(list(another_dir_list))) + ' elements:')
        for d in another_dir_list:
            print('>' + d.text)
        return [x.text for x in another_dir_list if len(x.text) > 0]

    def click_on_the_downloads_dir_check_box_button(self):
        return self.find_element(DemoQaCheckBoxPageLocators.LOCATOR_DOWNLOADS_DIR_CHECKBOX_BUTTON, time=10).click()

    def click_on_the_file_in_dir_check_box(self):
        return self.find_element(DemoQaCheckBoxPageLocators.LOCATOR_SELECT_FILE_IN_DOWNLOADS, time=10).click()

    def check_selected_files(self):
        slected_files_list = self.find_elements(DemoQaCheckBoxPageLocators.LOCATOR_CHECK_SELECTED_FILE, time=10)
        selected_files_str = '\n\n' + " ".join([x.text for x in slected_files_list])
        print(selected_files_str)
        return selected_files_str
