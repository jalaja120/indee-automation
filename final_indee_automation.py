from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

# Configuration
CHROMEDRIVER_PATH = r"C:\WebDrivers\chromedriver-win64\chromedriver.exe"
PIN_CODE = "WVMVHWBS"
URL = "https://indeedemo-fyc.watch.indee.tv/"

# Setup Chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
wait = WebDriverWait(driver, 20)

try:
    print("Launching platform...")
    driver.get(URL)

    # Step 1: Enter PIN and login
    pin_input = wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
    pin_input.send_keys(PIN_CODE + Keys.ENTER)
    print("PIN submitted.")
    time.sleep(4)

    # Step 2: Click the first video tile
    tiles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img")))
    if not tiles:
        raise Exception("No video tiles found.")
    driver.execute_script("arguments[0].scrollIntoView(true);", tiles[0])
    tiles[0].click()
    print("Video tile clicked.")
    time.sleep(5)

    # Step 3: Click play button
    play_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//svg[contains(@class, 'MuiSvgIcon-root')]")))
    play_button.click()
    print("Play button clicked.")
    time.sleep(5)

    # Step 4: Handle "Continue Watching" if it appears
    try:
        continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Continue Watching')]")))
        continue_btn.click()
        print("Continue Watching clicked.")
        time.sleep(5)
    except:
        print("Continue Watching not available.")

    # Step 5: Go back to home screen
    driver.back()
    print("Navigated back.")
    time.sleep(3)

    # Step 6: Attempt logout
    try:
        logout = wait.until(EC.element_to_be_clickable((By.ID, "signOutSideBar")))
        logout.click()
        print("Logged out.")
    except:
        print("Logout button not found.")

    print("Automation completed.")

except Exception as e:
    print("An error occurred:", e)
    traceback.print_exc()
    driver.save_screenshot("error.png")
    print("Saved screenshot as error.png for debugging.")

finally:
    input("Press ENTER to close browser...")
    driver.quit()
