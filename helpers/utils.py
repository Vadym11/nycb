import os, time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
date = datetime.now().strftime("%d-%m-%Y")
# ../../screenshot from current file dir
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "screenshot", str(date))

screenshot_name = 'test_run_at' + '-' + now + ".png"

def screen_path():
    global screen_dir
    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)
    return screen_dir


def save_screenshot(_browser):
    _browser.get_screenshot_as_file(os.path.join(screen_path(), screenshot_name))