from behave import given, when, then

@when('Hover over MAC')
def hover_over_mac(context):
    context.app.header.hover_over_mac()

@then('Click on Mabook Air')
def macbookair_click(context):
    context.app.header.macbookair_click()

@then('Verify review count to match with number of reviews')
def reviewcount_verify(context):
    context.app.header.macbookair_reviewcount_verify()