from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Set up Selenium WebDriver (Ensure you have downloaded the appropriate driver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Provide your LinkedIn credentials
username = driver.find_element(By.ID, 'username')
username.send_keys('your-email@example.com')

password = driver.find_element(By.ID, 'password')
password.send_keys('your-password')

# Log in
password.send_keys(Keys.RETURN)

# Allow time for login
time.sleep(5)

# List to store alumni data
alumni_data = []

# List of LinkedIn profile URLs to scrape
linkedin_urls = ['https://www.linkedin.com/in/sample-profile1', 'https://www.linkedin.com/in/sample-profile2']

# Loop through each LinkedIn profile URL
for url in linkedin_urls:
    driver.get(url)
    time.sleep(3)  # Allow the page to load

    # Scraping each data point
    try:
        name = driver.find_element(By.CSS_SELECTOR, 'li.inline.t-24.t-black.t-normal').text
    except:
        name = None

    try:
        job_title = driver.find_element(By.CSS_SELECTOR, 'h2.mt1.t-18.t-black.t-normal').text
    except:
        job_title = None

    try:
        employer = driver.find_element(By.CSS_SELECTOR, 'span.t-14.t-black.t-normal').text
    except:
        employer = None

    try:
        hometown = driver.find_element(By.CSS_SELECTOR, 'li.t-16.t-black.t-normal.inline-block').text
    except:
        hometown = None

    # Graduation date and/or major (from the Education section)
    try:
        education_section = driver.find_element(By.XPATH, "//section[contains(@id,'education')]")
        graduation_info = education_section.text  # You can further split this text if necessary
    except:
        graduation_info = None

    # LinkedIn profile URL
    linkedin_url = driver.current_url

    # Email (Check contact info if available)
    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Contact info').click()
        time.sleep(2)
        email = driver.find_element(By.XPATH, "//a[contains(@href, 'mailto:')]").text
    except:
        email = None

    # Add the data to the list
    alumni_data.append({
        'Name': name,
        'Hometown': hometown,
        'Employer': employer,
        'Job Title': job_title,
        'Email': email,
        'Graduation Info': graduation_info,
        'LinkedIn URL': linkedin_url
    })

    time.sleep(5)  # Avoid scraping too fast

# Convert the list to a DataFrame and save it as CSV
df = pd.DataFrame(alumni_data)
df.to_csv('alumni_data.csv', index=False)

# Close the browser
driver.quit()