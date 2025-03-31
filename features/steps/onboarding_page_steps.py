from behave import given, when, then

@given('Click to Skip onboarding')
def click_skip(context):
    context.app.onboarding_page.click_skip()