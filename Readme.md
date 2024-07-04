# NOTE: The app provided as part of the take_home task was not working for me thus I chose to go with saucedemo as an alternative.

---

# SauceDemo(https://www.saucedemo.com/) Automation Framework

This repository contains a comprehensive automation framework for testing the SauceDemo website, leveraging Playwright, Python, Allure Reports, and GitLab CI/CD.

## Project Structure

```
SauceDemoAutomation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
|   └── inventory_page.py
├── tests/
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   ├── test_product_page.py
│   └── test_checkout.py
├── utils/
│   ├── browser.py
│   ├── allure_utils.py
│   └── config.py
├── conftest.py
├── requirements.txt
└── .gitlab-ci.yml
```

- **pages/**: Contains Page Object Model (POM) classes for different pages of the SauceDemo website.
- **tests/**: Includes test scripts for various functionalities like login, add to cart, product page interaction, and checkout.
- **utils/**:
  - **browser.py**: Defines the Browser class and Playwright browser instance management.
  - **allure_utils.py**: Provides functions for attaching screenshots on test failures to Allure reports.
  - **config.py**: Centralizes configuration variables such as base URLs and credentials.
- **conftest.py**: Defines fixtures and hooks for the pytest test suite.
- **requirements.txt**: Lists Python dependencies.
- **.gitlab-ci.yml**: Configures GitLab CI/CD pipeline for automated testing and Allure report generation.

## Running the Tests

To run the tests locally:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/saucedemo-automation.git
   ```

2. Navigate to the project directory:
   ```
   cd saucedemo-automation
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run tests using pytest:
   ```
   pytest
   ```

This command will execute all tests and generate an Allure report.

To view the Allure report locally:

1. Install Allure CLI (if not already installed):
   ```
   # For macOS using Homebrew
   brew install allure

   # For Windows using Scoop
   scoop install allure
   ```

2. Serve the Allure report:
   ```
   allure serve allure-results
   ```

This will open the Allure report in your default web browser.

## GitLab CI/CD

The repository includes a `.gitlab-ci.yml` file that automates the testing process using GitLab CI/CD:

- Installs dependencies.
- Executes tests using pytest.
- Generates Allure report as artifacts.
- Serves the Allure report post-test execution.

To use the GitLab CI/CD pipeline:

1. Set up a GitLab repository.
2. Configure the pipeline in the GitLab web interface with appropriate runners.

## Test Structure

The test cases are organized into separate files based on functionalities:

- **test_login.py**: Tests for login functionality.
- **test_add_to_cart.py**: Tests for adding items to the cart.
- **test_product_page.py**: Tests for interacting with product pages.
- **test_checkout.py**: Tests for the checkout process.

Each test file utilizes the Page Object Model (POM) pattern for maintaining clear separation of concerns and ease of maintenance.

## Reporting

The framework integrates Allure Reports for detailed and visually appealing test reports. Screenshots are attached to reports on test failures using utility functions provided in `allure_utils.py`.

## Conclusion

This SauceDemo automation framework provides a robust solution for testing the SauceDemo(https://www.saucedemo.com/) website efficiently. The modular design, use of industry-standard tools, and seamless integration with GitLab CI/CD ensure reliability, scalability, and maintainability of the automation solution.

---

