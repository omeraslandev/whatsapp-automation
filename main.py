import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open WhatsApp web
driver.get('https://web.whatsapp.com')

# Login WhatsApp web
while True:
    verify = input("Did you login? (yes/no): ")
    if verify.lower() == "yes":
        break

# Entering profile section
profile_section = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/header/div/div[2]/div/div[2]/button/div/div/div/div/img')
profile_section.click()

def changing_pfp():
    pfp = random.randint(1, 48)
    profile_photo = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/div/span/div/div/div[1]/div/input')
    profile_photo.send_keys(f"C:\\Users\\omeer\\Desktop\\freepalestinebaby\\images\\{pfp}.jpg")

    time.sleep(1)

    zoom_out_pfp = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/button[2]/span')
    for _ in range(5):
        zoom_out_pfp.click()
        time.sleep(0.5)

    confirm_pfp = driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div[2]/span/div/div')
    confirm_pfp.click()

# Main loop
while True:
    changing_pfp()
    time.sleep(86400)