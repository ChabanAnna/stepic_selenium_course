from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
    new_w = browser.window_handles[1]
    browser.switch_to.window(new_w)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    ans_inp = browser.find_element_by_id("answer")
    ans_inp.send_keys(y)
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()
finally:
    time.sleep(12)
    browser.close()
