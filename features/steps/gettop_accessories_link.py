from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Gettop home page')
def open_gettop_homepage(context):
    context.app.main_page.open_mainpage()

@when('Hover over Accessories')
def hover_over_accessories(context):
    context.app.header.hover_over_accessories()

@then('Click on Cases&protections link')
def cases_protection_link(context):
    context.app.header.cases_protection_click()

@then('Verify 404 message is present')
def cases_protection_verify(context):
    context.app.header.cases_protection_404_verify()