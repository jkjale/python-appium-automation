from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from app.application import Application


def mobile_driver_init(context, scenario_name):
    """
    :param context: Behave context
    """

    ### Android ###
    # desired_capabilities = {
    #     "platformName": "Android",
    #     "automationName": 'uiautomator2',
    #     "platformVersion": "16",
    #     "deviceName": "Android Emulator",
    #     "appActivity": "org.wikipedia.main.MainActivity",
    #     "appPackage": "org.wikipedia",
    #     "app": "/Users/jakelee/Desktop/QA/python-appium-automation/mobile_app/uptodown-org.wikipedia.apk",
    #     "newCommandTimeout": 5000
    # }

    ### iOS ###
    desired_capabilities = {
        "platformName": "iOS",
        "automationName": 'XCUITest',
        "platformVersion": "18.3",
        "deviceName": "iPhone SE (3rd generation)",
        "appActivity": "org.wikipedia.main.MainActivity",
        "appPackage": "org.wikipedia",
        "app": "/Users/jakelee/Desktop/QA/python-appium-automation/mobile_app/uptodown-org.wikipedia.apk",
        "newCommandTimeout": 5000
    }

    appium_server_url = 'http://localhost:4723'
    ### Android ###
    # capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

    ### iOS ###
    capabilities_options = XCUITestOptions().load_capabilities(desired_capabilities)

    context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    context.driver.implicitly_wait(5)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    mobile_driver_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot(f'{step}.png')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
