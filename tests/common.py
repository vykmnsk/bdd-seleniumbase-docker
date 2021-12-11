from pytest_bdd import scenarios, given, when, then, parsers
import pytest


text_bot_or_not = "We can't tell if you're a human or a bot."
error_bot = "Encountered bot protection Captcha"


@given(parsers.parse('I am on "{tab_name}" tab'))
def nav_to_stays(sb, tab_name):
    sb.click_link(tab_name)


@then("I can see multiple listings")
def check_results(sb):
    if sb.is_text_visible(text_bot_or_not):
        pytest.xfail(error_bot)
    listings = sb.find_elements('a.listing__link')
    assert len(listings) > 1
