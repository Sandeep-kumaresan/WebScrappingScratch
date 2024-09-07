from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

# Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
service = Service('/home/sandeep/Downloads/chrome-headless-shell-linux64/chrome-headless-shell')  # Adjust path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the search URL
url = 'https://www.linkedin.com/jobs/search/?keywords=data%20science%20intern&location=New%20York'
driver.get(url)

# Extract job data
jobs = []
job_elements = driver.find_elements(By.CLASS_NAME, 'job-card-container')
for job in job_elements:
    title = job.find_element(By.CSS_SELECTOR, 'h3').text
    company = job.find_element(By.CSS_SELECTOR, 'a.job-card-container__company-name').text
    location = job.find_element(By.CSS_SELECTOR, 'span.job-card-container__metadata-item').text
    description = 'N/A'  # LinkedIn may not display full descriptions in search results

    jobs.append({
        'Title': title,
        'Company': company,
        'Location': location,
        'Description': description
    })

# Save to CSV
df = pd.DataFrame(jobs)
df.to_csv('jobs.csv', index=False)
print(f'Saved {len(jobs)} jobs to jobs.csv')

driver.quit()
