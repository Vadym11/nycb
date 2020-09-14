# from selenium import webdriver

from start_point import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from helpers import utils
from helpers.utils import screenshot_name

# This makes browser wait n seconds before presence of an element gets located
# The explicit function time.sleep(n) can also be used in every function as a substitute - "import time" in this case needed
wait = WebDriverWait(browser, 5)

def feb_cn (class_n):
    try:
        link = wait.until(EC.presence_of_element_located((By.CLASS_NAME, class_n)))
    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
        utils.save_screenshot(browser)
        browser.quit()
        assert False, 'check out screenshot ' + screenshot_name
    return link.click()

def feb_lt (link_t):
    try:
        link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_t)))
    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
        utils.save_screenshot(browser)
        browser.quit()
        assert False, 'check out screenshot ' + screenshot_name
    return link.click()

def feb_xp (xp):
    try:
        link = wait.until(EC.presence_of_element_located((By.XPATH, xp)))
    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
        utils.save_screenshot(browser)
        browser.quit()
        assert False, 'check out screenshot ' + screenshot_name
    return link.click()

def feb_id (id):
    try:
        link = wait.until(EC.presence_of_element_located((By.ID, id)))
    except (TimeoutException, ElementClickInterceptedException, NoSuchElementException):
        utils.save_screenshot(browser)
        browser.quit()
        assert False, 'check out screenshot ' + screenshot_name
    return link.click()