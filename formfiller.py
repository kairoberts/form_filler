from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.kairoberts.dev")
driver.maximize_window()

time.sleep(1)

button = driver.find_element_by_link_text("Contact")
button.click()

try:
    contact_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    )
    contact_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    contact_subject = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "subject"))
    )
    contact_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    contact_name.click()
    contact_name.send_keys("Kai Roberts")

    contact_email.click()
    contact_email.send_keys("test@test.com")

    contact_subject.click()
    contact_subject.send_keys("Automated Message")

    contact_message.click()
    contact_message.send_keys(
        "This is an automated python script sending this message from your website")

    submit = driver.find_element_by_id("contact-btn")
    submit.click()

    time.sleep(2)

    driver.back()

    time.sleep(1)


finally:
    driver.quit()
