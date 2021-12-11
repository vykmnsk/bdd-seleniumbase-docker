from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from common import *


nav_signin = "//button[contains(., 'Sign in')]"
nav_signin_popup = 'Sign in'

login_header = 'h1'
login_header_text = 'Sign in'
login_email_box = '#loginFormEmailInput'
login_password_box = '#loginFormPasswordInput'
login_button = '#loginFormSubmitButton'
login_error_banner = '#loginFormErrorBanner'

text_bot_or_not = "We can't tell if you're a human or a bot."
prompt_human_help = 'manually verify not a robot and hit <Enter>'


scenarios('features/Login.feature')


@given("I don't have valid username and password",
       target_fixture="user_pwd_invalid")
def user_pwd_invalid():
    return ('invalid@example.email', 'invalid_password')


@when("I try to sign in")
def try_sign_in(sb, user_pwd_invalid):
    user, password = user_pwd_invalid

    sb.click(nav_signin)
    sb.click_link(nav_signin_popup)
    if sb.is_text_visible(text_bot_or_not):
        pytest.fail(error_bot)
    sb.assert_text(login_header_text, login_header)

    sb.update_text(login_email_box, user)
    sb.update_text(login_password_box, password)
    sb.click(login_button)


@then(parsers.parse('I get error "{msg}"'))
def verify_err_message(sb, msg):
    sb.assert_element_visible(login_error_banner)
    sb.assert_text_visible(msg)
