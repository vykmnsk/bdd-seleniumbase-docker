from pytest_bdd import scenarios, when, then, parsers
import pytest
from common import *


scenarios('features/Stays.feature')

btn_to = "button[aria-label='Going to']"
input_to = '#location-field-destination'
btn_search = '[data-testid="submit-button"]'
lnk_listing = 'a.listing__link'


@when(parsers.parse('I search for "{location}"'))
def search_stays(sb, location):
    sb.click(btn_to)
    sb.update_text(input_to, location+'\n')
    sb.click(btn_search)

@then("I can see multiple listings")
def check_results(sb):
    if sb.is_text_visible(text_bot_or_not):
        pytest.xfail(error_bot)
    listings = sb.find_elements(lnk_listing)
    assert len(listings) > 1


@then("I can pick 1st listing")
def pick_listing1(sb):
    sb.click(lnk_listing)
