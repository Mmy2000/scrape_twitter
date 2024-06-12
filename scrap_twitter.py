import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver

def scrape_twitter(accounts, ticker, interval):
    driver = init_driver()
    try:
        total_mentions = 0
        for account in accounts:
            retries = 3
            while retries > 0:
                try:
                    url = f"https://x.com/{account}"
                    logging.info(f"Accessing {url}")
                    driver.get(url)
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                    time.sleep(5)  # Giving some time for the page to fully load
                    page_source = driver.page_source
                    mentions = page_source.count(ticker)
                    total_mentions += mentions
                    logging.info(f"'{ticker}' was mentioned '{mentions}' times on {account}.")
                    break  # Exit the retry loop if successful
                except Exception as e:
                    logging.error(f"Error accessing {account}: {e}")
                    retries -= 1
                    if retries == 0:
                        logging.error(f"Failed to access {account} after multiple attempts.")
        logging.info(f"'{ticker}' was mentioned a total of '{total_mentions}' times in the last '{interval}' minutes.")
    finally:
        driver.quit()


accounts = [
    "Mr_Derivatives", "warrior_0719", "ChartingProdigy", "allstarcharts",
    "yuriymatso", "TriggerTrades", "AdamMancini4", "CordovaTrades",
    "Barchart", "RoyLMattox"
]

ticker = "$TSLA"
interval = 15

scrape_twitter(accounts, ticker, interval)


# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager

# # # Initialize the Chrome driver
# # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# # # Open the website
# # driver.get("https://www.google.com")

# # # Find the search box element by name
# # search_box = driver.find_element(By.NAME, "q")

# # # Enter a search query
# # search_box.send_keys("Selenium WebDriver")

# # # Simulate pressing the Enter key
# # search_box.send_keys(Keys.RETURN)

# # # Wait for the results to load
# # driver.implicitly_wait(10)  # Implicit wait for 10 seconds

# # # Get the first result title
# # first_result = driver.find_element(By.CSS_SELECTOR, "h3")
# # print(first_result.text)

# # # Close the browser
# # driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import logging
# import time

# # Set up logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def init_driver():
#     options = webdriver.ChromeOptions()
#     # options.add_argument("--headless")  # Disable headless mode
#     # options.add_argument("--disable-gpu")  # Disable GPU
#     # options.add_argument("start-maximized")  # Maximize the window
#     # options.add_argument("disable-infobars")  # Disable infobars
#     # options.add_argument("--disable-extensions")  # Disable extensions
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     return driver

# def scrape_twitter(accounts, ticker, interval):
#     driver = init_driver()
#     try:
#         total_mentions = 0
#         for account in accounts:
#             retries = 3
#             while retries > 0:
#                 try:
#                     url = f"https://x.com/{account}"
#                     logging.info(f"Accessing {url}")
#                     driver.get(url)
#                     WebDriverWait(driver, 10).until(
#                         EC.presence_of_element_located((By.TAG_NAME, "body"))
#                     )
#                     time.sleep(5)  # Giving some time for the page to fully load
#                     page_source = driver.page_source
#                     mentions = page_source.count(ticker)
#                     total_mentions += mentions
#                     logging.info(f"'{ticker}' was mentioned '{mentions}' times on {account}.")
#                     break  # Exit the retry loop if successful
#                 except Exception as e:
#                     logging.error(f"Error accessing {account}: {e}")
#                     retries -= 1
#                     if retries == 0:
#                         logging.error(f"Failed to access {account} after multiple attempts.")
#         logging.info(f"'{ticker}' was mentioned a total of '{total_mentions}' times in the last '{interval}' minutes.")
#     finally:
#         driver.quit()

# accounts = [
#     "Mr_Derivatives", "warrior_0719", "ChartingProdigy", "allstarcharts",
#     "yuriymatso", "TriggerTrades", "AdamMancini4", "CordovaTrades",
#     "Barchart", "RoyLMattox"
# ]

# ticker = "$TSLA"
# interval = 15

# scrape_twitter(accounts, ticker, interval)
