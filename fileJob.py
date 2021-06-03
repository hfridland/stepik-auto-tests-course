from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el_firstname = browser.find_element_by_name("firstname")
    el_firstname.send_keys("Ivan")
    el_lastname = browser.find_element_by_name("lastname")
    el_lastname.send_keys("Petrov")
    el_email = browser.find_element_by_name("email")
    el_email.send_keys("ipetrov@hotmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    el_file = browser.find_element_by_name("file")
    el_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
