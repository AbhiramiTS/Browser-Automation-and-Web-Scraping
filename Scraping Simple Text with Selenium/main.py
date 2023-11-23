"""
Web Scraping Script

This script uses Selenium with Chrome WebDriver to automate web browsing and extract text content from a
specific element on a webpage.

Functions:
- `get_driver()`: Initializes a Chrome WebDriver with customized options for easier browsing and navigates
    to a specified URL.
- `main()`: Calls `get_driver()` to set up the WebDriver, finds a specific HTML element using XPath,
    and returns the text content of that element.

Usage:
- Ensure that the Selenium package is installed (`pip install selenium`).
- Make sure you have the Chrome WebDriver executable in your system's PATH.
- Run the script to perform automated browsing and text extraction.

Note:
- The script is configured for the website "http://automated.pythonanywhere.com" and extracts text from the element
    located at "/html/body/div[1]/div/h1[1]" using XPath.
- Adjust the URL and XPath values in the script as needed for different websites or elements.

"""

from selenium import webdriver


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


print(main())
