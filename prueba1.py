from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")


#PARTE 1 (ANGIE ELLIS)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("laptop hp pavilion")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.CLASS_NAME, "s-image").click()

#PARTE 2 (DEREK STANZIOLA)
driver.find_element(By.ID, 'a-autoid-0-announce').click()
driver.find_element(By.ID, 'quantity_3').click()
driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.ID, "sw-gtc").click()

time.sleep(100)
driver.close()
