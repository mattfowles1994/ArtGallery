
import os
import pytest
from pytest_bdd import scenarios, given, when, parsers, then

scenarios('../features/gallery.feature')

@when('I select add artwork')
def select_add_listing(browser, live_server):
    browser.links.find_by_partial_href(f'/artwork/add/').click()

@when(parsers.parse('I add a piece of artwork with the name "{title}"'))
def add_artwork(browser, live_server, title):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    browser.fill('title', title)
    browser.fill('price', 20)
    browser.fill('width', 30)
    browser.fill('height', 40)

@then('Then I see the artwork "{title}" was added successfully. message')
def step_impl(context):
    br = context.browser
    assert br.current_url.endswith('/admin/artwork/artwork/')