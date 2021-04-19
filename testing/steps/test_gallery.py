
import os
import pytest
from pytest_bdd import scenarios, given, when, parsers, then
import time

scenarios('../features/gallery.feature')

@when('I select add artwork')
def select_add_listing(browser, live_server, client, admin_user):

    browser.links.find_by_partial_href(f'/artwork/add/').click()


@when(parsers.parse('I add a piece of artwork with the name "{title}"'))
def add_artwork(browser, live_server, title):
    browser.fill('title', title)
    browser.fill('price', 20)
    browser.fill('width', 30)
    browser.fill('height', 40)
    browser.find_by_name(f'_save').click()
    #time.sleep(20)

#@then(parsers.parse('I see the "{title}" is in the list'))
#def verify_artwork_added(browser, title):
#    assert browser.links.find_by_text(title)