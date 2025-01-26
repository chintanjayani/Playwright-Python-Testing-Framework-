import pytest
from pages.home_page import HomePage

@pytest.mark.ui
def test_home_page_loads(page):
    homepage = HomePage(page)
    homepage.navigate()

    assert "Restful-booker-platform demo" in page.title()

@pytest.mark.ui
def test_home_page_welcome_message(page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.wait_for_selector("//div[@class='row hotel-description']/div/p")
    expected_welcome_message = "Welcome to Shady Meadows, a delightful Bed & Breakfast nestled in the hills on Newingtonfordburyshire. A place so beautiful you will never want to leave. All our rooms have comfortable beds and we provide breakfast from the locally sourced supermarket. It is a delightful place."

    assert expected_welcome_message in homepage.welcome_message_loc.text_content(), f"Actual text '{homepage.welcome_message_loc.text_content()}' does not contain expected text '{expected_welcome_message}'"

@pytest.mark.ui
def test_home_page_footer(page):
    homepage = HomePage(page)
    homepage.navigate()
    expexted_footer = "restful-booker-platform v1.7.0 Created by Mark Winteringham - © 2019-24 Cookie-Policy - Privacy-Policy - Admin panel"

    assert expexted_footer in homepage.footer_loc.text_content()

@pytest.mark.ui
def test_home_page_logo_visibility(page):
    homepage = HomePage(page)
    homepage.navigate()
    homepage.wait_for_selector(homepage.logo_loc)
    logo = page.locator(homepage.logo_loc)
    is_logo_visible = logo.is_visible()
    
    assert is_logo_visible == True, "Logo is not visible"


@pytest.mark.ui
def test_cookie_policy_url(page):
    homepage = HomePage(page)
    homepage.navigate()
    page.get_by_text("Cookie-Policy").click()
    homepage.wait_for_selector(homepage.cookie_page_text_loc)
    
    assert "Cookie Policy" in page.text_content("body")

@pytest.mark.ui
def test_privacy_policy_url(page):
    homepage = HomePage(page)
    homepage.navigate()
    page.get_by_text("Privacy-Policy").click()
    homepage.wait_for_selector(homepage.privacy_policy_page_text_loc)
    
    assert "Privacy Policy Notice" in page.text_content("body")
