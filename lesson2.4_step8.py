from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, 'book'), '10000 RUR')
    )

button.click()
