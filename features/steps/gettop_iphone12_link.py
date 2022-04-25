from behave import given, when, then

@then('Hover over IPHONE drop down menu')
def hover_iphone(context):
    context.app.header.hover_over_iphone()

@then('Click on iPhone 12 link')
def iphone12_click(context):
    context.app.header.iphone12_link_click()