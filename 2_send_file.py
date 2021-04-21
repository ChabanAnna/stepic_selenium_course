import os
from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements_by_css_selector("input[type='text']")
    for el in elements:
        el.send_keys("AAA")
    file_element = browser.find_element_by_css_selector("input[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    file_element.send_keys(file_path)
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
finally:
    time.sleep(20)
    browser.close()
