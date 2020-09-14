from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/Users/vadym.tymeichuk/Coursera/SE/chromedriver')
browser.get('https://nycitybride.com')
page = browser.find_element_by_link_text('Contact Us')
page.click()
# try:
#     elem = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.ID, "input_search"))
#     )
fh = open('titles.txt', 'w+')
try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'input_search'))
    )
    elem.send_keys('wedding veil')
    elem.send_keys(Keys.RETURN)
except:
    browser.quit()

try:
    class0 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "recent-post-list"))
    )
    items = class0.find_elements_by_class_name ("recent-post-item")
    for item in items:
        title = item.find_element_by_tag_name ('h4')
        print(title.text)
        fh.write(title.text + '\n')
finally:
    browser.quit()
fh.close()
# print(type(browser.page_source))
# time.sleep(5)

# browser.quit()