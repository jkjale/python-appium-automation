from pages.base_page import Page
from pages.home_page import HomePage
from pages.onboarding_page import OnboardingPage
from pages.search_page import SearchPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.home_page = HomePage(driver)
        self.onboarding_page = OnboardingPage(driver)
        self.search_page = SearchPage(driver)
