from pytest_bdd import scenarios, given, when, then, parsers


text_bot_or_not = "We can't tell if you're a human or a bot."
prompt_human_help = 'manually verify not a robot and hit <Enter>'


scenarios('../features/Stays.feature')


@given(parsers.parse('I am on "{tab_name}" tab'))
def nav_to_stays(sb, tab_name):
    sb.click_link(tab_name)


@when(parsers.parse('I search for "{location}"'))
def search(sb, location):
    sb.click("button[aria-label='Going to']")
    sb.update_text('#location-field-destination', location+'\n')
    sb.click('[data-testid="submit-button"]')


@then("I can see multiple listings")
def check_results(sb):
    if sb.is_text_visible(text_bot_or_not):
        input(prompt_human_help)
    listings = sb.find_elements('a.listing__link')
    assert len(listings) > 1
