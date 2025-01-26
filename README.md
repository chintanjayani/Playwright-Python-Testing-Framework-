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

## Bugs

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

