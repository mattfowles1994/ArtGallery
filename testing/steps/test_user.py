
import os
import pytest
from pytest_bdd import scenarios, given, when, parsers, then
import time

scenarios('../features/user.feature')

@when('I select add user')
def select_add_listing(browser, live_server, client, admin_user):

    browser.links.find_by_partial_href(f'/user/add/').click()


@when(parsers.parse('I enter details of an item with the name "{title}"'))
def add_artwork(browser, live_server, title):
    browser.fill('username', title)
    browser.fill('password1', 'abacus123')
    browser.fill('password2', 'abacus123')
    browser.find_by_name(f'_save').click()

@when(parsers.parse('I enter same details for username and password'))
def add_artwork(browser, live_server):
    browser.fill('username', 'abacus123')
    browser.fill('password1', 'abacus123')
    browser.fill('password2', 'abacus123')
    browser.find_by_name(f'_save').click()

@when(parsers.parse('I enter amended details'))
def add_artwork(browser, live_server):
    browser.fill('first_name', 'abacus123')
    browser.fill('last_name', 'abacus123')
    browser.find_by_name(f'_save').click()
