import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://my.asoiu.edu.az/student/courses/10025")

    # --- MANUAL LOGIN STEP ---
    print("Please log in manually in the browser window...")
    # This gives you 30 seconds to type your username/password and hit enter
    time.sleep(100) 
    # -------------------------

    # Now wait for the topics to appear after you've logged in
    wait = WebDriverWait(driver, 15)
    topics = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list-group-item")))

    all_topics = [t.text.strip().split('\n') for t in topics]
    print(all_topics)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()

s =0 
for  i in all_topics:
    i = int(i)
    s+=i
print(s)