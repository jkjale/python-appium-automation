from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

desired_capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "platformVersion": "16",
    "deviceName": "Android Emulator",
    "appActivity": "org.wikipedia.main.MainActivity",
    "appPackage": "org.wikipedia",
    "app": "/Users/jakelee/Desktop/QA/python-appium-automation/mobile_app/uptodown-org.wikipedia.apk",
    "newCommandTimeout": 5000
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)

driver.find_element(AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()

driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Search Wikipedia"]').click()

driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Python (programming language)')

actual_text = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="org.wikipedia:id/page_list_item_title" and @text="Python (programming language)"]').text
expected_text = 'Python (programming language)'

assert actual_text == expected_text, f'Expected {actual_text} but got {expected_text}'

driver.quit()