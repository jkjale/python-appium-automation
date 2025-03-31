from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import Page


class SearchPage(Page):
    FIRST_RESULT = (AppiumBy.XPATH, '//*[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]')
    SEARCH_BAR = (AppiumBy.ID, 'org.wikipedia:id/search_src_text')
    SEARCH_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Search Wikipedia"]')

    def click_search_bar(self):
        self.wait_until_clickable_click(self.SEARCH_BUTTON)

    def input_search_word(self, search_word):
        self.input_text(search_word, *self.SEARCH_BAR)

    def verify_first_result(self, search_word):
        self.wait_until_visible(self.FIRST_RESULT)
        self.verify_text(search_word, *self.FIRST_RESULT)