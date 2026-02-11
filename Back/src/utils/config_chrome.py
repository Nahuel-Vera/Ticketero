from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def selenium_config():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service()  # usa chromedriver del PATH
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver


def run_browser(driver):
    driver.get("https://www.google.com")

    time.sleep(5)
    close_browser(driver)
    return {"status": "Browser opened and navigated to Google"}


def close_browser(driver):
    driver.quit()