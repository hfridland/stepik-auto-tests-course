from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_x = browser.find_element_by_id("input_value")
    x = element_x.text
    y = calc(x)

    element_answer = browser.find_element_by_id("answer")
    element_answer.send_keys(y)

    element_robot_cb = browser.find_element_by_id("robotCheckbox")
    element_robot_cb.click()

    element_robot_rb = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element_robot_rb)
    element_robot_rb.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
