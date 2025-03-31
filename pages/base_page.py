from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(f'{name}.png')

    def wait_until_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )

    def wait_until_clickable_click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element not clickable by {locator}'
        )
        element.click()

    def wait_until_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element not visible by {locator}'
        )

    def wait_until_all_are_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message=f'Elements not visible by {locator}'
        )

    def wait_until_invisible(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element still visible by {locator}'
        )

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text.strip().lower()
        assert expected_text.lower() == actual_text, f'Expected "{expected_text}" is not "{actual_text}"'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text.lower()
        assert expected_text.lower() in actual_text, f'Expected "{expected_text}" not in "{actual_text}"'

    def close(self):
        self.driver.close()
