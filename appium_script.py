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
    "newCommandTimeout": 1000
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)

# driver.find_element(AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button').click()
#
# driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Search Wikipedia']").click()
#
# driver.find_element(AppiumBy.ID, 'org.wikipedia:id/search_src_text').send_keys('Python (programming language)')
#
# expected_result = 'Python (programming language)'
# actual_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text
#
# assert actual_result == expected_result, f'Expected {expected_result} did not match actual {actual_result}'
#
# driver.quit()
