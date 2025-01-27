# Playwright Python Test Automation Framework

A cross-platform test automation framework using Python and Playwright.


## Prerequisites and Local Setup Guide
- Python 3.8+
- pip
- Git

1. Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install
   ```
   
4. Install Node if want to run performance tests locally 
    ```bash
    # installs nvm (Node Version Manager)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
    # download and install Node.js (you may need to restart the terminal)
    nvm install 22
    npm -v
    #install artillery
    npm install -g artillery
    #Cmd to run performance tests locally
    artillery run tests/performance\ /performance-test.yaml 
    ```

5. Install following if want to run accessibility tests locally 
   ```bash
   npm install puppeteer axe-core @axe-core/puppeteer
   #Cmd to run accessiblity tests
   node tests/accessiblity\ /accessibility-test.js
   ```


## Running Tests
To run all tests:
```bash
pytest --html=reports/report.html
```
or
```bash
python run_tests.py
```

To run specific test categories:
```bash
pytest -m ui --html=reports/report.html  # UI tests only
pytest -m api --html=reports/report.html  # API tests only
```

### Note: All the UI test runs in headless mode, to enable run with a browser set HEADLESS=false in .env file

## Test Reports
- HTML reports are generated in the `reports` directory after each test run

## CI/CD Integration
This framework includes GitHub Actions configuration for automated test execution on push and pull requests.


## Test Coverage
High-priority areas covered:
1. Home page UI checks 
2. Contact form UI validation scenarios
3. Booking page UI validation scenarios
4. Admin page UI validation scenarios
5. Sample API tests for Rooms endpoint
6. Performance tests for Rooms endpoint
7. Accessiblity tests

## Framework Features Overview
1. Page Object Model design pattern
2. Separate UI and API test suites
3. Config management for different environments
4. HTML report generation
5. CI/CD integration with GitHub Actions
6. Screenshots on failures
7. Performance tests with Artillery in CI/CD and Locally
8. Automated Accessiblity testing in CI/CD and Locally
9. Environment variables support for variable configs


## Future Test Areas
- E2E Booking functionality
- Pagination
- Mobile responsiveness
- Performance metrics (SLO/SLIs)
- Cross-browser testing
- Advanced booking scenarios
- Advanced API test coverage
- Hotel room photos check
- Broken images/links UI checks
- User/Admin E2E tests
- Security testing for UI/API
- Localization tests


# Test Plan (High Level)

## 1. Objectives
- **Verify** that all functionalities of the booking system operate as intended.
- **Ensure** the platform's APIs respond correctly to various requests.
- **Assess** the performance of the application under different load conditions.
- **Identify and address** security vulnerabilities.
- **Evaluate** the user interface for usability and accessibility.

## 2. Scope

### In-Scope:
- **Functional Testing**: Booking creation, modification, and deletion.
- **API Testing**: Endpoints related to bookings, rooms, authentication, reporting, and messaging.
- **Performance Testing**: Under various user loads.
- **Security Testing**: Including authentication mechanisms and data protection.
- **Usability Testing**: Evaluation of the user interface.

## 3. Test Strategy

### 3.1 Functional Testing

- **Booking Management**:
  - Create a new booking with valid data and verify its presence in the system.
  - Modify an existing booking and confirm the changes are saved.
  - Delete a booking and ensure it is removed from the system.

- **Authentication**:
  - Test login functionality with valid and invalid credentials.
  - Verify access restrictions for authenticated and unauthenticated users.

- **Messaging**:
  - Send a message through the contact form and verify its receipt in the admin panel.

### 3.2 API Testing
- Utilize tools like **Postman** to test API endpoints.
- Verify responses for various HTTP methods (GET, POST, PUT, DELETE) on booking-related endpoints.
- Check for appropriate status codes and response times.

### 3.3 Performance Testing
- Conduct **load testing** to assess how the application performs under a high number of simultaneous users.
- Monitor response times and system behavior during peak loads.

### 3.4 Security Testing
- Perform vulnerability scanning to identify common security issues.
- Test for **SQL injection**, **cross-site scripting (XSS)**, and **cross-site request forgery (CSRF)**.
- Ensure sensitive data, such as passwords, are encrypted.

### 3.5 Usability Testing
- Evaluate the **user interface** for intuitive navigation and design consistency.
- Ensure that forms provide clear validation messages and guidance.
- Assess the application's **accessibility features**.

## 4. Test Environment
- **Browsers**: Latest versions of Chrome, Firefox, Safari, and Edge.
- **Devices**: Desktop, tablet, and mobile devices with various screen resolutions.
- **Tools**: 
  - Postman for API testing.
  - JMeter for performance testing.
  - OWASP ZAP for security testing.

## 5. Test Data
- Create test data sets for bookings, including edge cases with boundary values.
- Use both valid and invalid data to test form validations and error handling.

## 6. Test Execution
- Execute test cases in the designated test environment.
- Log defects with detailed steps to reproduce, expected results, and actual results.
- Prioritize defects based on severity and impact.

## 7. Deliverables
- Test cases and scripts.
- Test execution reports.
- Defect logs with status updates.
- Performance and security assessment reports.

---

# Bugs

### 1. Bug Title: **Past Dates Selectable in Room Booking Calendar**
- **Description**: Users are able to select past dates while making a room booking, which should not be allowed.
- **Severity**: High
- **Steps to Reproduce**:
  1. Navigate to the room booking calendar.
  2. Attempt to select a past date for the booking.
- **Actual Result**: Past dates can be selected, allowing users to book rooms for dates that have already passed.
- **Expected Result**: Past dates should be disabled or not selectable in the calendar.

---

### 2. Bug Title: **Booking Validation Not Proper**
- **Description**: The room booking validation logic is not functioning as expected.
- **Severity**: High
- **Steps to Reproduce**:
  1. Attempt to book a room without filling in all required fields.
  2. Submit the form.
- **Actual Result**: The system does not properly validate missing or incorrect data.
- **Expected Result**: All required fields should be validated, and appropriate error messages should be displayed if fields are incomplete or incorrect.

---

### 3. Bug Title: **Anyone Can Book the Room**
- **Description**: There is no user authentication or validation, allowing anyone to book a room.
- **Severity**: High
- **Steps to Reproduce**:
  1. Navigate to the booking page.
  2. Book a room without signing in or providing any user credentials.
- **Actual Result**: A room can be booked by anyone without any authentication or user validation.
- **Expected Result**: Only authenticated or registered users should be able to make a booking.

---

### 4. Bug Title: **Hotel Booking Dates Not Selectable, Calendar Drag Working But Select Not**
- **Description**: The calendar used for selecting hotel booking dates is malfunctioning as users can drag to select dates, but the manual date selection (clicking on a specific date) does not work.
- **Severity**: Medium
- **Steps to Reproduce**:
  1. Navigate to the hotel booking page.
  2. Try to select a date by clicking on it in the calendar.
  3. Drag to select a date range.
- **Actual Result**: The date cannot be selected manually by clicking, but dragging to select a range works.
- **Expected Result**: Users should be able to select a date manually by clicking on a specific date, and dragging should also function normally.

---

### 5. Bug Title: **Incorrect Error Messages on Contact Forms**
- **Description**: The error messages displayed during invalid bookings and form submissions are not appropriate.
- **Severity**: Medium
- **Steps to Reproduce**:
  1. Submit the booking form or the contact form with invalid data (e.g., invalid email, missing fields).
- **Actual Result**: Unclear or incorrect error messages are displayed.
- **Expected Result**: Error messages should be clear, informative, and specific to the validation issue (e.g., “Please enter a valid email address”).

---

### 6. Bug Title: **Email and Phone Validation Issues**
- **Description**: The email field accepts invalid emails without ".com," and the phone number field accepts alphanumeric and special characters.
- **Severity**: High
- **Steps to Reproduce**:
  1. Enter an email without a ".com" in the email field.
  2. Enter alphanumeric or special characters in the phone number field.
- **Actual Result**: The email field accepts invalid entries, and the phone number field accepts unwanted characters.
- **Expected Result**: The email field should only accept valid email formats, and the phone number field should only accept numeric values.

---

### 7. Bug Title: **Inconsistent Fonts in Room Title**
- **Description**: There are inconsistencies in the fonts used for room titles.
- **Severity**: Low
- **Steps to Reproduce**:
  1. Navigate to a room listing page.
  2. Check the font style of the room title.
- **Actual Result**: The font used for room titles is inconsistent across different pages or elements.
- **Expected Result**: The room title should have consistent font styling throughout the website.

---

### 8. Bug Title: **Missing Title for Contact Form Area**
- **Description**: The Contact form area does not have a title or label.
- **Severity**: Low
- **Steps to Reproduce**:
  1. Navigate to the contact page.
  2. Look for the title of the contact form section.
- **Actual Result**: The Contact form area is missing a title.
- **Expected Result**: The contact form should have a clear title such as "Contact Us."

---

### 9. Bug Title: **Room Creation Allows Identical Room Names**
- **Description**: The system allows the creation of rooms with identical names.
- **Severity**: High
- **Steps to Reproduce**:
  1. Log into the admin portal and navigate to the Rooms tab.
  2. Create a room with a specific name.
  3. Create another room with the same name.
- **Actual Result**: The system allows the creation of multiple rooms with the same name.
- **Expected Result**: Room names should be unique, and the system should reject attempts to create rooms with identical names.

---

### 10. Bug Title: **Unable to Add Image to Existing Room Number**
- **Description**: When trying to create a room with an existing room number, the image cannot be added.
- **Severity**: High
- **Steps to Reproduce**:
  1. Navigate to the admin portal and go to the Rooms tab.
  2. Enter a room number that already exists.
  3. Try to add an image to the room.
- **Actual Result**: The system allows the creation of a room with an existing number but does not allow adding an image.
- **Expected Result**: The system should prevent the creation of rooms with duplicate room numbers, and image upload functionality should work properly.

---

### 11. Bug Title: **No Error Message for Invalid Admin Credentials**
- **Description**: No error message is displayed when invalid credentials are entered during admin login.
- **Severity**: High
- **Steps to Reproduce**:
  1. Navigate to the admin login page.
  2. Enter invalid credentials (e.g., incorrect username/password).
- **Actual Result**: No error message is displayed when invalid credentials are entered.
- **Expected Result**: The system should display a clear error message when invalid credentials are entered, such as "Invalid username or password."

---

### 12. Bug Title: **Large Name Data Submittable in Contact Form**
- **Description**: The Contact form allows the submission of excessively large data in the "Name" field.
- **Severity**: Medium
- **Steps to Reproduce**:
  1. Fill out the contact form with an extremely large string in the "Name" field.
  2. Submit the form.
- **Actual Result**: The form allows submission with large data in the "Name" field, which may break the layout.
- **Expected Result**: There should be a character limit or validation for the "Name" field to prevent large data submission.

---

### 13. Bug Title: **Static Map in Footer**
- **Description**: The map displayed in the footer is static and cannot be interacted with.
- **Severity**: Low
- **Steps to Reproduce**:
  1. Scroll to the footer of the website.
  2. Try to interact with the map.
- **Actual Result**: The map is static and cannot be zoomed or interacted with.
- **Expected Result**: The map should be interactive, allowing users to zoom and explore.

---

### 14. Bug Title: **Incorrect Copyright Year in Footer**
- **Description**: The copyright year in the footer is incorrect and outdated.
- **Severity**: Low
- **Steps to Reproduce**:
  1. Scroll to the footer of the website.
  2. Check the copyright year.
- **Actual Result**: The copyright year is outdated or incorrect.
- **Expected Result**: The copyright
