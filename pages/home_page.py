from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcome_message_loc = self.page.locator("//div[@class='row hotel-description']/div/p")
        self.footer_loc = self.page.locator("//p[@class='text-muted']")
        self.contact_form_loc = self.page.locator("//div[@class='row contact']/div[3]")
        self.logo_loc = "img.hotel-logoUrl"
        self.cookie_link_loc = self.page.locator("//a[@href='/#/cookie']")
        self.cookie_page_text_loc = "//*[text()='Cookie Policy']"
        self.privacy_policy_page_text_loc = "//*[text()='Privacy Policy Notice']"
        self.contact_submit_button_loc = self.page.locator("//*[@id='submitContact']")
        self.contact_submit_success_message_loc = "//*[@class='row contact']/div[2]/div"
        self.contact_submit_invalid_input_message_loc = self.page.locator("//*[@class='alert alert-danger']")
        self.booking_room_button_loc = self.page.locator("(//button[text()='Book this room'])[1]")
        self.booking_room_book_button_loc = self.page.locator("//button[text()='Book']")
        self.booking_calendar_loc = self.page.locator("div[class*='rbc-day-bg']")

        self.contact_name = "ContactName"
        self.contact_email = "ContactEmail"
        self.contact_phone = "ContactPhone"
        self.contact_subject = "ContactSubject"
        self.contact_desc = "ContactDescription"

        self.booking_first_name = "//*[@name='firstname']"
        self.booking_last_name = "//*[@name='lastname']"
        self.booking_email = "//*[@name='email']"
        self.booking_phone = "//*[@name='phone']"

    def navigate(self):
        super().navigate()

    def fill_contact_form(self, name, email, phone, subject, desc):
        page = self.page
        page.get_by_test_id(self.contact_name).fill(name)
        page.get_by_test_id(self.contact_email).fill(email)
        page.get_by_test_id(self.contact_phone).fill(phone)
        page.get_by_test_id(self.contact_subject).fill(subject)
        page.get_by_test_id(self.contact_desc).fill(desc)
    
    def fill_booking_form(self, first_name, last_name, email, phone):
        page = self.page
        page.locator(self.booking_first_name).fill(first_name)
        page.locator(self.booking_last_name).fill(last_name)
        page.locator(self.booking_email).fill(email)
        page.locator(self.booking_phone).fill(phone)
        