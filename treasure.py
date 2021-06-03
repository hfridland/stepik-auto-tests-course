from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    cb_robot = browser.find_element_by_id("robotCheckbox")
    cb_robot.click()
    rb_robots_rule = browser.find_element_by_id("robotsRule")
    rb_robots_rule.click()

    btn_submit = browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()


finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
