"""

Web Scraping Script

This script utilizes Selenium with Chrome WebDriver to automate web browsing,
extract dynamic content from a specified element on a webpage, and perform additional processing.

Functions:
- `get_driver()`: Initializes a Chrome WebDriver with customized options for enhanced browsing and navigates
  to a predefined URL.
- `clean_text(text: str) -> float`: Extracts and cleans the temperature information from the given text,
  returning it as a floating-point number.
- `main() -> float`: Executes the main workflow by setting up the WebDriver, introducing a delay for page loading,
  locating the target element using XPath, and extracting and cleaning the temperature text.

Usage:
- Ensure that the Selenium package is installed (`pip install selenium`).
- Ensure the Chrome WebDriver executable is in the system's PATH.
- Run the script to perform automated browsing, extract temperature information, and display the result.

Note:
- The script is configured for the website "http://automated.pythonanywhere.com" and extracts temperature information
  from the element located at "/html/body/div[1]/div/h1[2]" using XPath.
- Adjust the URL, XPath, or other parameters in the script as needed for different websites or elements.


"""


from selenium import webdriver
import time


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


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


print(main())
