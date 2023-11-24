"""

Automated Login Script

This script utilizes the Selenium library to automate the login process on a specific website
(http://automated.pythonanywhere.com/login/). The script performs the following steps:

1. Initializes a Chrome WebDriver with specific options to ease browsing.
2. Navigates to the login page of the website.
3. Enters the username "automated" into the corresponding input field.
4. Waits for 2 seconds to simulate user interaction.
5. Enters the password "automatedautomated" into the password input field and presses Enter.
6. Waits for another 2 seconds.
7. Clicks on a specific navigation link identified by its XPath.
8. Prints the current URL after the navigation.

Dependencies:
- Selenium (webdriver)
- time

Note: This script is specific to the structure of the provided website.
Adjustments may be required for different websites or changes in the website's structure.

Usage:
Run the script to automate the login process and print the current URL after successful navigation.

"""




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)


main()
