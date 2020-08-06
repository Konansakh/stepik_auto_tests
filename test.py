from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def fun(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element_by_tag_name("button")
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button.click()

x = browser.find_element_by_id("input_value").text
result = fun(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

button = browser.find_element_by_id("solve")
button.click()