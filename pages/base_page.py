from faker import Faker
class BasePage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://automationintesting.online"

    def navigate(self, path=""):
        self.page.goto(f"{self.base_url}{path}")

    def wait_for_selector(self, selector, timeout=5000):
        return self.page.wait_for_selector(selector, timeout=timeout)

    def test_data_generator(self):
        fake = Faker()
        self.name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.phone = fake.phone_number()
        self.subject = fake.pystr(5,10)
        self.message = fake.pystr(21, 199)
        self.uuid = fake.pyint()


