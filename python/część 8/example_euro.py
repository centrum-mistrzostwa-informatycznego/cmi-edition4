import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
today = date.today()
browser = webdriver.Firefox()

browser.get("https://www.euro.com.pl/")
time.sleep(1)
try:    
    accept_policy = browser.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_policy.click()
except NoSuchElementException:
    pass
time.sleep(1)

tv_button = browser.find_element(By.XPATH, '//ul[@id="top-menu"]/li/a[contains(text(),"TV")]')
action = webdriver.ActionChains(browser)
action.move_to_element(tv_button)
action.perform()
time.sleep(1)
plasma_page = browser.find_element(By.XPATH, '//ul[@id="second-menu"]//a[contains(@href,"plazmowe")]')
plasma_page.click()
time.sleep(5)

xpath1 = '//div[@id="products"]/div[@class="product-for-list"]'
xpath2_int = '(//div[@id="products"]/div[@class="product-for-list"])[{}]'
name_suffix = '//h2[@class="product-name"]/a'
price_suffix = '//div[contains(@class, "price-normal")]'

items_on_page = len(browser.find_elements(By.XPATH, xpath1))
for i in range(items_on_page):
    name = browser.find_element(By.XPATH,xpath2_int.format(i+1)+name_suffix).get_attribute("text").strip()
    price = browser.find_element(By.XPATH,xpath2_int.format(i+1)+price_suffix).get_attribute("innerHTML").replace('&nbsp;',' ').strip()
    print(f'Produkt: {name} był w cenie {price} dnia {today}')

time.sleep(10)
browser.close()