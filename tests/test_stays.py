from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from common import *

scenarios('features/Stays.feature')

btn_to = "button[aria-label='Going to']"
input_to = '#location-field-destination'
btn_search = '[data-testid="submit-button"]'


@when(parsers.parse('I search for "{location}"'))
def search_stays(sb, location):
    sb.click(btn_to)
    sb.update_text(input_to, location+'\n')
    sb.click(btn_search)
