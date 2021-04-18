from django.core.management import call_command
from selenium import webdriver
import pytest

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass

@pytest.fixture(scope='session', autouse=True)
def splinter_webdriver():
    """Override splinter webdriver name."""
    return 'chrome'


#@pytest.fixture()
#def django_db_setup(django_db_setup, django_db_blocker):
#    # Load test db
#    with django_db_blocker.unblock():
#        call_command('loaddata', '../db.json')