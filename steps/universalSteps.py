from behave import *
from selectors.fields import fields
from selectors.elements import elements

pages = {
    'google': 'www.google.pl'
}


def set_locator_parameter(selector, argument):
    return selector.replace('{argument}', argument)

@given(u'I am on {pagename} page')
def impl(context, pagename):
    context.driver.visit(context.base_url + pages[pagename])

@when(u'I fill field {fieldname} with text {text}')
def step_impl(context, fieldname, text):
    context.driver.find_element(fields[fieldname]).send_keys(text)

@when(u'I click element {element}')
def step_impl(context, element):
    context.driver.find_element(elements[element]).click()

@when(u'I click element {element} with argument {argument}')
def step_impl(context, element, argument):
    context.driver.find_element(set_locator_parameter(elements[element], argument)).click()

@then(u'I should see element {element} contains value bigger then {value}')
def imple(context, element, value):
    assert int(context.driver.find_element(elements[element]).text) == int(value)