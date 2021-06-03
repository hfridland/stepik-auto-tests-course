from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    num = int(num1.text) + int(num2.text)

    browser.find_element_by_id("dropdown").click()
    browser.find_element_by_css_selector(f"[value='{num}']").click()

    btn_submit = browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
