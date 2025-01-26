import pytest
import datetime
from pages.home_page import HomePage

@pytest.mark.ui
def test_contact_form_info(page):
    homepage = HomePage(page)
    homepage.navigate()
    expected_contact_details = "Shady Meadows B&B The Old Farmhouse, Shady Street, Newfordburyshire, NE1 410S 012345678901 fake@fakeemail.com"

    assert expected_contact_details in homepage.contact_form_loc.text_content()


@pytest.mark.ui
def test_contact_form_submission_successfully(page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.test_data_generator()
    homepage.fill_contact_form(homepage.name, homepage.email, homepage.phone, homepage.subject, homepage.message)
    homepage.contact_submit_button_loc.click()

    actual_mesage = page.text_content(homepage.contact_submit_success_message_loc)
    expected_message = f"Thanks for getting in touch {homepage.name}!We'll get back to you about{homepage.subject}as soon as possible."
    
    assert expected_message == actual_mesage


@pytest.mark.ui
def test_contact_form_submission_with_invalid_name(page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.test_data_generator()
    homepage.fill_contact_form("", homepage.email, homepage.phone, homepage.subject, homepage.message)
    homepage.contact_submit_button_loc.click()
    
    assert "Name may not be blank" in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
def test_contact_form_submission_with_invalid_email(page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.test_data_generator()
    homepage.fill_contact_form(homepage.name, "skjfhsdiekd", homepage.phone, homepage.subject, homepage.message)
    homepage.contact_submit_button_loc.click()
    
    assert "must be a well-formed email address" in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
@pytest.mark.parametrize(
    "phone, expected_error_message",
    [
        ("", "Phone may not be blank"),
        ("4738390000", "Phone must be between 11 and 21 characters."),
        ("1" * 22, "Phone must be between 11 and 21 characters."),
    ],
)
def test_contact_form_submission_with_invaild_number(page, phone, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.test_data_generator()
    homepage.fill_contact_form(homepage.name, homepage.email, phone, homepage.subject, homepage.message)
    homepage.contact_submit_button_loc.click()
    
    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
@pytest.mark.parametrize(
    "message, expected_error_message",
    [
        ("", "Subject may not be blank"),
        ("shor", "Subject must be between 5 and 100 characters."),
        ("a" * 101, "Subject must be between 5 and 100 characters."),
    ],
)
def test_contact_form_submission_with_invaild_subject(page, message, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.test_data_generator()
    homepage.fill_contact_form(homepage.name, homepage.email, homepage.phone, message, homepage.message)
    homepage.contact_submit_button_loc.click()
    
    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
@pytest.mark.parametrize(
    "message, expected_error_message",
    [
        ("", "Message may not be blank"),
        ("short", "Message must be between 20 and 2000 characters."),
        ("a" * 2001, "Message must be between 20 and 2000 characters."),
    ],
)
def test_contact_form_submission_with_invaild_message(page, message, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.test_data_generator()
    homepage.fill_contact_form(homepage.name, homepage.email, homepage.phone, homepage.subject, message)
    homepage.contact_submit_button_loc.click()
    
    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()