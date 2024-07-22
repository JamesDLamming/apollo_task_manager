from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv()

apollo_username= os.getenv('apollo_username')
apollo_password= os.getenv('apollo_password')
linkedIn_username = os.getenv('linkedIn_username')
linkedIn_password = os.getenv('linkedIn_password')
# Get today's date
today = datetime.now()

# Format it as "YYYY-MM-DD"
formatted_date = today.strftime("%Y-%m-%d")



# Create a new Chrome browser instance
apollo_url = "https://app.apollo.io/#/tasks?userIds[]=current&finderViewId=6418428dc6d5b9008b1d2054&taskTypeCds[]=linkedin_actions&page=1&dateRange[max]="+formatted_date


# Open apollo LI tasks webpage
driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/login")
time.sleep(15)
username_field = driver.find_element(By.ID,"username")
password_field = driver.find_element(By.ID,"password")

username_field.send_keys(linkedIn_username)
password_field.send_keys(linkedIn_password)
time.sleep(3)
password_field.send_keys(Keys.RETURN)

time.sleep(10)





driver.get(apollo_url)

time.sleep(10)
username_field = driver.find_element(By.NAME,"email")
password_field = driver.find_element(By.NAME,"password")
username_field.send_keys(apollo_username)
password_field.send_keys(apollo_password)
time.sleep(3)
password_field.send_keys(Keys.RETURN)

time.sleep(20)

# Navigate to first task

first_task = driver.find_elements(By.CLASS_NAME,('zp_j37Z8'))[0]
first_task.click()

# Run loop while complete task element id is present

complete_task_element = driver.find_elements(By.XPATH,("//*[text()='Complete Task']"))[0]

while complete_task_element:

  # If this is a call or connection request, skip
  
  # Find elements
  phone_element = []
  email_element = []
  connection_element = []
  phone_element = driver.find_elements(By.XPATH,("//*[contains(text(), 'Log Call')]"))
  email_element = driver.find_elements(By.XPATH,("//*[contains(text(), 'Schedule')]"))
  connection_element = driver.find_elements(By.XPATH,("//*[contains(text(), 'Copy Text')]"))
  
  
  if phone_element or email_element or connection_element:
    # click next button
    next_button = driver.find_elements(By.XPATH,("//i[@class='zp-icon apollo-icon apollo-icon-caret-right zp_dZ0gM zp_j49HX zp_uAV5p']"))[0]
    next_button.click()
    time.sleep(3)
  else:
    

    # Find the link using its text (you can also use link's id, class, etc.)
    link = driver.find_elements(By.XPATH,("//button[@class='zp-button zp_zUY3r zp_n9QPr zp_eFcMr zp_f6llr']"))[0]
  
    # Open the link in a new tab using CTRL + click
    link.send_keys(Keys.CONTROL + Keys.RETURN)
    
    # Switch to the new tab (assuming it's the next one to the right)
    driver.switch_to.window(driver.window_handles[1])
    
    
    # Scroll down by 500 pixels
    time.sleep(1)
    scroll_random = str(random.randint(500,2000))
    driver.execute_script("window.scrollBy(0, "+scroll_random+");")
    
    # Wait for a few seconds
    time.sleep(random.randint(10,25))
    
    # Close the current tab
    driver.close()
    
    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])
    
    # Complete task
    
    complete_link = driver.find_elements(By.XPATH,("//*[contains(text(), 'Complete Task')]"))[0]
    
    complete_link.click()
    time.sleep(3)
  # Repeat until all tasks completed
  complete_task_element = driver.find_elements(By.XPATH,("//*[text()='Complete Task']"))[0]

# It's a good practice to quit the driver after use
driver.quit()
