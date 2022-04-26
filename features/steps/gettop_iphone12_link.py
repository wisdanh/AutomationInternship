from behave import given, when, then

@then('Hover over IPHONE drop down menu')
def hover_iphone(context):
    context.app.header.hover_over_iphone()

@then('Click on iPhone 12 link')
def iphone12_click(context):
    context.app.header.iphone12_link_click()

@then('Verify iphone 12 is in the url')
def iphone12_link_verify(context):
    query = 'iphone-12'
    context.app.header.iphone12_link_verify(query)
    print(f'iphone')