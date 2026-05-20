A lightweight Python automation tool that logs into the my.asoiu.edu.az portal to fetch and aggregate topic information from specific course modules.

🛠 Features
Automated Navigation: Directly targets specific course IDs.

Manual Login Support: Includes a 100-second grace period for secure manual authentication (no need to store passwords in your code).

Data Extraction: Scrapes items from the course list group.

Calculation: Attempts to parse and sum extracted numerical values from the topics.

📋 Prerequisites
Before running the script, ensure you have the following installed:

Python 3.x

Google Chrome

Selenium Library

ChromeDriver (matching your Chrome version)

🚀 Getting Started
1. Installation
First, install the Selenium dependency:

Bash
pip install selenium
2. Configuration
The script is currently set to target a specific course ID. You can modify the URL in the driver.get() line to target a different course:

Python
driver.get("https://my.asoiu.edu.az/student/courses/YOUR_COURSE_ID")
3. Usage
Run the script via your terminal:

Bash
python scraper.py
A Chrome window will open.

Manually enter your ASOIU credentials and log in.

The script will wait for 100 seconds (or until you finish) before scraping the data.

Once finished, it will output the scraped topics and their sum to the console.

⚠️ Important Notes
Data Parsing: The script currently expects the extracted text to be convertible to integers. If your course topics contain non-numeric text, ensure you modify the for loop logic to prevent ValueError.

Wait Times: The time.sleep(100) is a placeholder for manual login. You can shorten this once you are comfortable with the login speed.

Ethical Use: This tool should be used for personal academic purposes only. Do not use it to overwhelm university servers.

📄 License
Distributed under the MIT License. See LICENSE for more information.

Disclaimer: This project is not officially affiliated with or endorsed by Azerbaijan State Oil and Industry University (ASOIU).
