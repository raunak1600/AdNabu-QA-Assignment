from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://adnabu-store-assignment1.myshopify.com")
driver.find_element(By.ID, "password").send_keys("AdNabuQA")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//details-modal[@class='header__search']").click()
driver.find_element(By.ID, "Search-In-Modal").send_keys("snowboard")
driver.find_element(By.XPATH,"//button[@aria-label='Search']").click()
element = driver.find_element(By.XPATH,"(//div[@class='card__content'])[3]")
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.find_element(By.LINK_TEXT,"The Complete Snowboard").click()
driver.find_element(By.XPATH,"//button[@name='add']").click()
print("Item Added to Cart Successfully")
driver.quit()
