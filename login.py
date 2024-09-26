from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Chrome in this case)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Provide your LinkedIn credentials
#CHANGE THIS TO YOURS
username = driver.find_element_by_id('username')
username.send_keys('your-email@example.com')

#CHANGE THIS TO YOURS
password = driver.find_element_by_id('password')
password.send_keys('your-password')

# Log in
password.send_keys(Keys.RETURN)

# Allow time for login
time.sleep(5)