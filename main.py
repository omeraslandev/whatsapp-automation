import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

time.sleep(5)

# Open WhatsApp web
driver.get('https://web.whatsapp.com')

# Login WhatsApp web
while True:
    verify = input("Do you login Whatsapp Web sir ?\n\n\n")
    if verify=="yes":
        break

# Entering profile section
profile_section = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/header/div/div[2]/div/div[2]/button/div/div/div/div/img')

profile_section.click()

def changing_pfp():
    # Choosing random pfp
    pfp = random.randint(1,48)

    # Generate random durations
    hours = random.randint(0, 1)  # Between 0 and 2 hours
    minutes = random.randint(0, 59)  # Between 0 and 59 minutes
    seconds = random.randint(0, 59)  # Between 0 and 2 seconds
    milliseconds = random.randint(0, 999)  # Between 0 and 999 milliseconds
    microseconds = random.randint(0, 999999)  # Between 0 and 999,999 microseconds

    # Convert total time to seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000) + (microseconds / 1000000)

    # Print the duration in a formatted way
    print(f"Bekleme süresi: {hours} hours {minutes} minutes {seconds} seconds {milliseconds} milliseconds {microseconds} microseconds")

    # Upload new pfp
    profile_photo = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/div/span/div/div/div[1]/div/input')

    profile_photo.send_keys(f"C:\\Users\\omeer\\Desktop\\freepalestinebaby\\images\\{pfp}.jpg")

    time.sleep(1)

    # Recent edits
    zoom_out_pfp = driver.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/button[2]/span')

    for i in range(5):
        zoom_out_pfp.click()

    time.sleep(1)

    # Confirm new pfp
    confirm_pfp = driver.find_element(By.XPATH,'//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div/div[2]/span/div/div')

    confirm_pfp.click()

    # Sleep using time.sleep() with the calculated duration
    time.sleep(total_seconds)

while True:
    changing_pfp()