nav_signin = "//button[contains(., 'Sign in')]"
nav_signin_popup = 'Sign in'

login_header = 'h1'
login_header_text = 'Sign in'
login_email_box = '#loginFormEmailInput'
login_password_box = '#loginFormPasswordInput'
login_button = '#loginFormSubmitButton'
login_error_banner = '#loginFormErrorBanner'
login_error_banner_text = "Email and password don't match. Try again."

text_bot_or_not = "We can't tell if you're a human or a bot."
prompt_human_help = 'manually verify not a robot'
user_invalid = 'invalid@example.email'
password_invalid = 'invalid_password'


def test_invalid_signin(sb):
    sb.click(nav_signin)
    sb.click_link(nav_signin_popup)
    if sb.is_text_visible(text_bot_or_not):
        input(prompt_human_help)
        # breakpoint()
    sb.assert_text(login_header_text, login_header)

    do_signin(sb, user_invalid, password_invalid)

    sb.assert_element_visible(login_error_banner)
    sb.assert_text_visible(login_error_banner_text)

def do_signin(sb, user, password):
    sb.update_text(login_email_box, user)
    sb.update_text(login_password_box, password)
    sb.click(login_button)
