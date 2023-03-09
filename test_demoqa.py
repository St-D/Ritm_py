#  -*- coding: cp1251 -*-                                                                                             #
# Python 3.x.x

from demoqa_index_page import IndexPage
from demoqa_element_page import ElementPage
from demoqa_checkbox_page import CheckBoxPage, DemoQaCheckBoxPageLocators


def test_demoqa(browser):
    demoqa_main_page = IndexPage(browser)
    demoqa_main_page.go_to_site()
    assert "DEMOQA" in demoqa_main_page.driver.title
    demoqa_main_page.click_on_the_elements_icon()


# def test_demoqa_elements(browser):
    demoqa_elements_page = ElementPage(browser)
    assert "elements" in demoqa_elements_page.driver.current_url
    demoqa_elements_page.click_on_the_check_box_icon()


# def test_demoqa_check_box(browser):
    demoqa_check_box_page = CheckBoxPage(browser)
    assert "checkbox" in demoqa_check_box_page.driver.current_url
    demoqa_check_box_page.click_on_the_root_check_box_tree_button()

    check_box_locators = DemoQaCheckBoxPageLocators
    dir_after_click_list = demoqa_check_box_page.find_tree_elements(lctr=check_box_locators.LOCATOR_OTHER_DIR)
    assert 'Home' and 'Desktop' and 'Documents' and 'Downloads' in dir_after_click_list

    demoqa_check_box_page.click_on_the_downloads_dir_check_box_button()

    files_in_downloads_dir_list = demoqa_check_box_page.find_tree_elements(lctr=check_box_locators.LOCATOR_FILES_IN_DOWNLOADS)
    assert 'Word File.doc' and 'Excel File.doc' in files_in_downloads_dir_list

    demoqa_check_box_page.click_on_the_file_in_dir_check_box()
    selected_files = demoqa_check_box_page.check_selected_files()
    assert "You have selected : wordFile" in selected_files


# def main():
#     test_demoqa()
#     test_demoqa_elements()
#     test_demoqa_check_box()
#
#
# if __name__ == '__main__':
#     main()
