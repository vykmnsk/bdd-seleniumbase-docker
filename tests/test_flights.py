from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from common import *


scenarios('features/Flights.feature')

btn_from = "button[aria-label='Leaving from']"
btn_to = "button[aria-label='Going to']"
input_from = '#location-field-leg1-origin'
input_to = '#location-field-leg1-destination'
btn_search = '[data-testid="submit-button"]'



@when(parsers.parse('I search for flights from "{loc_from}" to "{loc_to}"'))
def search_flights(sb, loc_from, loc_to):
    sb.click(btn_from)
    sb.update_text(input_from, loc_from+'\n')
    sb.click(btn_to)
    sb.update_text(input_to, loc_to+'\n')
    sb.click(btn_search)
