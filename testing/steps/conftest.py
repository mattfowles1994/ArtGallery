from django.core.management import call_command
from selenium import webdriver
from pytest_bdd import given, then, parsers, when
import pytest

#@pytest.fixture(autouse=True)
#def enable_db_access_for_all_tests(db):
#    pass

@pytest.fixture(scope='session', autouse=True)
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'chrome'


@pytest.fixture()
def django_db_setup(django_db_setup, django_db_blocker):
    # Load test db
    with django_db_blocker.unblock():
        call_command('loaddata', 'testing/db.json')


@given('an admin user is logged in')
def admin_login(browser, client, live_server, db):
    client.login(username='matt', password='goodison')
    cookie = client.cookies['sessionid']
    
    browser.visit(live_server.url + '/admin/')
    browser.cookies.add({'sessionid': cookie.value})
    browser.reload()

@then(parsers.parse('I see the "{title}" is in the list'))
def verify_artwork_added(browser, title):
    assert browser.links.find_by_text(title)

@then(parsers.parse('I see the confirmation'))
def verify_artwork_added(browser):
    assert browser.find_by_css('.success')

@then(parsers.parse('I see the error'))
def verify_artwork_added(browser):
    assert browser.find_by_css('.errornote')

@when(parsers.parse('I select "{item}"'))
def view_artworks(browser, live_server, item):
    browser.links.find_by_text(item).first.click()

@when('I confirm')
def view_artworks(browser, live_server):
    browser.find_by_value('Yes, I’m sure').click()
