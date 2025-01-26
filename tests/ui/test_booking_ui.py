import pytest
from pages.home_page import HomePage

@pytest.mark.ui
def test_hotel_booking(page):
    homepage = HomePage(page)
    homepage.navigate()

    homepage.booking_room_button_loc.click()
    homepage.wait_for_selector("div[class*='calendar']")
    days = homepage.booking_calendar_loc

    start_day = days.nth(7) 
    end_day = days.nth(10)

    # start_day.hover()
    # page.mouse.down()
    # end_day.hover()
    # page.mouse.up()

    homepage.test_data_generator()
    homepage.fill_booking_form(homepage.name, homepage.last_name, homepage.email, homepage.phone)
    homepage.booking_room_book_button_loc.click()


@pytest.mark.ui
@pytest.mark.parametrize(
    "first_name, expected_error_message",
    [
        ("", "Firstname should not be blank"),
        ("ab", "size must be between 3 and 18"),
        ("b" * 19, "size must be between 3 and 18"),
    ],
)
def test_hotel_booking_with_invalid_first_name(page, first_name, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.booking_room_button_loc.click()

    homepage.test_data_generator()
    homepage.fill_booking_form(first_name, homepage.last_name, homepage.email, homepage.phone)
    homepage.booking_room_book_button_loc.click()

    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
@pytest.mark.parametrize(
    "last_name, expected_error_message",
    [
        ("", "Lastname should not be blank"),
        ("ab", "size must be between 3 and 30"),
        ("b" * 31, "size must be between 3 and 30"),
    ],
)
def test_hotel_booking_with_invalid_last_name(page, last_name, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.booking_room_button_loc.click()

    homepage.test_data_generator()
    homepage.fill_booking_form(homepage.name, last_name, homepage.email, homepage.phone)
    homepage.booking_room_book_button_loc.click()

    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
@pytest.mark.parametrize(
    "email, expected_error_message",
    [
        ("", "must not be empty"),
        ("sjdadj", "must be a well-formed email address"),
    ],
)
def test_hotel_booking_with_invalid_email(page, email, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.booking_room_button_loc.click()

    homepage.test_data_generator()
    homepage.fill_booking_form(homepage.name, homepage.last_name, email, homepage.phone)
    homepage.booking_room_book_button_loc.click()

    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()


@pytest.mark.ui
@pytest.mark.parametrize(
    "phone, expected_error_message",
    [
        ("", "must not be empty"),
        ("2"*10, "size must be between 11 and 21"),
        ("1"*22, "size must be between 11 and 21"),
    ],
)
def test_hotel_booking_with_invalid_phone(page, phone, expected_error_message):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.booking_room_button_loc.click()

    homepage.test_data_generator()
    homepage.fill_booking_form(homepage.name, homepage.last_name, homepage.email, phone)
    homepage.booking_room_book_button_loc.click()

    assert expected_error_message in homepage.contact_submit_invalid_input_message_loc.text_content()

