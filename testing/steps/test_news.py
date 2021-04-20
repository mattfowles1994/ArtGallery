
import os
import pytest
from pytest_bdd import scenarios, given, when, parsers, then
import time

scenarios('../features/news.feature')

@when('I select add news')
def select_add_listing(browser, live_server, client, admin_user):

    browser.links.find_by_partial_href(f'/new/add/').click()


@when(parsers.parse('I enter details of an item with the name "{title}"'))
def add_artwork(browser, live_server, title):
    browser.fill('eventname', title)
    browser.fill('eventcomment', 'test news comment')
    browser.find_by_name(f'_save').click()

@when(parsers.parse('I enter same details for username and password'))
def add_artwork(browser, live_server):
    browser.fill('username', 'abacus123')
    browser.fill('password1', 'abacus123')
    browser.fill('password2', 'abacus123')
    browser.find_by_name(f'_save').click()

@when(parsers.parse('I enter amended details'))
def add_artwork(browser, live_server):
    browser.fill('eventname', 'new')
    browser.find_by_name(f'_save').click()
