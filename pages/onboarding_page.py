from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import Page


class OnboardingPage(Page):
    SKIP_BUTTON = (AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')

    def click_skip(self):
        self.wait_until_clickable_click(self.SKIP_BUTTON)
