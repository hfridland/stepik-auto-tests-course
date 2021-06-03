from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    element_x = browser.find_element_by_id("input_value")
    x = element_x.text
    y = calc(x)

    element_answer = browser.find_element_by_id("answer")
    element_answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
