from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service(r"D:\PYTHON_PROJECT\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[type=password]").send_keys("admin123")
#driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()

# time.sleep(5)
# assert "dashboard" in driver.current_url
# driver.find_element(By.XPATH,"//a[contains(text(),'Welcome')]").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()
# assert "login" in driver.current_url

#driver.find_element(By.LINK_TEXT,"Forgot your password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()
# print(driver.current_url)
# assert 'Reset' in driver.current_url

driver.find_element(By.TAG_NAME,"a").click()
print(driver.current_url)
assert 'Reset' in driver.current_url


#driver.quit()
# driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
# driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "button").click()

# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_class_name("button").click()
