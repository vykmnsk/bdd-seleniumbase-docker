from pytest_bdd import scenarios, when, then, parsers
from common import *


scenarios('features/Flights.feature')

btn_from = "button[aria-label='Leaving from']"
btn_to = "button[aria-label='Going to']"
input_from = '#location-field-leg1-origin'
input_to = '#location-field-leg1-destination'
btn_search = '[data-testid="submit-button"]'

btn_flight = 'button[data-test-id="select-link"]'
btn_select = 'button[data-test-id="select-button"]'


@when(parsers.parse('I search for flights from "{loc_from}" to "{loc_to}"'))
def search_flights(sb, loc_from, loc_to):
    sb.click(btn_from)
    sb.update_text(input_from, loc_from+'\n')
    sb.click(btn_to)
    sb.update_text(input_to, loc_to+'\n')
    sb.click(btn_search)


@then("I can see multiple flights")
def check_results(sb):
    if sb.is_text_visible(text_bot_or_not):
        pytest.xfail(error_bot)
    flights = sb.find_elements(btn_flight)
    assert len(flights) > 1


@then("I can choose 1st flight")
def pick_listing1(sb):
    sb.click(btn_flight)
    sb.assert_element_visible(btn_select)
