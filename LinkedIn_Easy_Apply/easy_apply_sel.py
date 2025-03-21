from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv
load_dotenv()

# LinkedIn credentials
linkedin_username = os.getenv("email")
linkedin_password = os.getenv("pass")
# resume_path = r"/Users/pratik/Desktop/Resume/Pratik_Shankar_Jadhav.pdf"

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open in maximized window

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
def login_linkedin():
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(linkedin_username)
    driver.find_element(By.ID, "password").send_keys(linkedin_password, Keys.RETURN)
    print("Logged in to LinkedIn.")

def search_jobs(keyword="AI", location="United States"):
    """ Searches for jobs with 'Easy Apply' filter enabled """
    time.sleep(5)
    driver.get("https://www.linkedin.com/jobs/search/")
    time.sleep(10)  # Wait for the page to load
    print("Searched")
    try:
        # Find job search input field
        job_search_box = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search by title, skill, or company']"))
        )
        job_search_box.clear()
        job_search_box.send_keys(keyword)
        time.sleep(1)
        job_search_box.send_keys(Keys.RETURN) 
        time.sleep(2)
        easy_apply_filter_xpath = "//button[contains(@aria-label, 'Easy Apply')]"
        try:
            easy_apply_filter = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, easy_apply_filter_xpath))
            )
            easy_apply_filter.click()
            time.sleep(3)
            print(f"Filtering Easy Apply jobs for: {keyword} in {location}")
        except:
            print("No Easy Apply filter found.")
    except Exception as e:
        print(f"Error in job search: {e}")


def apply_to_jobs():
    # job_listings = driver.find_elements(By.TAG_NAME, "ul")
    job_listings = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
    for job in job_listings[:1]:  # Apply to the first 5 jobs
        try:
            
            # job_card = job.find_element(By.CLASS_NAME, "job-card-container--clickable")
            job.click()
            time.sleep(3)
            
            # Click "Easy Apply" if available
            easy_apply_btn = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(driver.find_element(By.CLASS_NAME, "jobs-apply-button"))
            )
            easy_apply_btn.click()
            time.sleep(3)
        

            # Click Next or Submit (depends on LinkedIn flow)
            next_btns = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'next')]")
            if next_btns:
                for next_btn in next_btns:
                    next_btn.click()
                    time.sleep(2)
            
            submit_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'submit')]"))
            )
            submit_btn.click()
            time.sleep(30)
            
            print("Applied to a job successfully!")
            break
        except Exception as e:
            continue
            print(f"Skipping a job due to error: {e}")
        time.sleep(3)

if __name__ == "__main__":
    login_linkedin()
    search_jobs("AI", "United States")
    apply_to_jobs()
    driver.quit()
    print("Job applications completed.")