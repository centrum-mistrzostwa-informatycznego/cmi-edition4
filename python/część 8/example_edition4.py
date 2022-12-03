## kawałek kodu który z użyciem tego geckodrivera obsługuje naszą pocztę

## do pracy z czymś takim służyć nam będzie biblioteka o nazwie Selenium

import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

def wyslij(dokogo, temat, co):
    browser = webdriver.Firefox()

    browser.get('https://profil.wp.pl/login/login.html')
    time.sleep(0.5)

    accept_button = browser.find_element(By.XPATH, '//button[text()="AKCEPTUJĘ I PRZECHODZĘ DO SERWISU"]')
    accept_button.click()

    time.sleep(1)

    login_field = browser.find_element(By.ID, 'login')
    login_field.send_keys("edycja.czwarta@wp.pl")

    password_field = browser.find_element(By.ID, 'password')
    password_field.send_keys("")

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

    time.sleep(1)

    napisz_button = browser.find_element(By.XPATH, '//button[text()="napisz"]')
    napisz_button.click()
    time.sleep(1)

    receipent_field = browser.find_element(By.XPATH, '//input[@value=""]')
    receipent_field.send_keys(dokogo)

    subject_field = browser.find_element(By.XPATH,'//input[@name="subject"]')
    subject_field.send_keys(temat)


    time.sleep(5)

    editor_div = browser.find_element(By.XPATH, '//div[@class="DraftEditor-editorContainer"]')
    editor_div.send_keys(co)
    # time.sleep(5)
    time.sleep(1)
    send_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    send_button.click()

    time.sleep(2)
    browser.close()

for i in range(100):
    wyslij('janeknowakowski13@wp.pl', f'wiadomosc {i}', f"Pozdrawiam po raz {i}")