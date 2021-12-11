from pytest_bdd import given, then, parsers
import pytest


text_bot_or_not = "We can't tell if you're a human or a bot."
error_bot = "Encountered bot protection Captcha"


@given(parsers.parse('I am on "{tab_name}" tab'))
def nav_to_tab(sb, tab_name):
    sb.click_link(tab_name)
