import pytest
import random
from pages.base_page import BasePage

@pytest.mark.ui
def test_admin_page_login(page):
    basepage = BasePage(page)
    basepage.navigate("/#/admin")

    page.get_by_test_id("username").fill("admin")
    page.get_by_test_id("password").fill("password")
    page.get_by_test_id("submit").click()

    assert "B&B Booking Management" in page.text_content("body")

@pytest.mark.ui
def test_hotel_room_creation(page):
    basepage = BasePage(page)
    basepage.navigate("/#/admin")

    uuid = str(random.randrange(999))
    page.get_by_test_id("username").fill("admin")
    page.get_by_test_id("password").fill("password")
    page.get_by_test_id("submit").click()

    page.get_by_test_id("roomName").fill(uuid)
    page.locator("//*[@id='roomPrice']").fill(uuid)
    page.locator("//*[@id='createRoom']").click()
    expected_message = page.locator(f"(//*[text()='{uuid}'])[1]").text_content()

    assert uuid in expected_message, f"{uuid} not found"