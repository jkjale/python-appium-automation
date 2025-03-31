from behave import given, when, then

@when('Click Search bar')
def click_search_bar(context):
    context.app.search_page.click_search_bar()

@when('Search for "{search_word}"')
def input_search_word(context, search_word):
    context.app.search_page.input_search_word(search_word)

@then('Verify first result is "{search_word}"')
def verify_first_result(context, search_word):
    context.app.search_page.verify_first_result(search_word)