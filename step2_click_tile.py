from selenium import webdriver
from selenium.webdriver.common.by import By  # Used for locating elements using strategies like ID, XPATH, etc.
from selenium.webdriver.support.ui import WebDriverWait  # Helps us wait for certain conditions (like element visible)
from selenium.webdriver.support import expected_conditions as EC  # Defines conditions to wait for
from selenium.webdriver.chrome.service import Service  # Used to set the path to chromedriver
import time  # Used for sleep delays

# ✅ STEP 1: Set up the path to your ChromeDriver executable
driver_path = "C:\\WebDrivers\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=driver_path)

# ✅ STEP 2: Launch Chrome browser using the Selenium driver
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Optional: Makes browser full screen for better element visibility

try:
    # ✅ STEP 3: Open the target Indee platform URL
    driver.get("https://indeedemo-fyc.watch.indee.tv/")
    wait = WebDriverWait(driver, 20)  # Sets max wait time for locating elements

    # ✅ STEP 4: Wait for the PIN input field to be present on the page
    print("🔄 Waiting for PIN input...")
    pin_input = wait.until(EC.presence_of_element_located((By.ID, "pin")))
    pin_input.send_keys("WVMVHWBS")  # Enters your assigned PIN

    # ✅ STEP 5: Wait for the SIGN IN button and click it
    print("🔄 Waiting for SIGN IN button...")
    sign_in_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Sign In']")
    ))
    sign_in_button.click()  # Clicks the Sign In button
    print("✅ Signed in successfully!")

    # ✅ STEP 6: Wait for the dashboard to load and locate the tile titled "Test automation project"
    print("🔄 Waiting for 'Test automation project' tile...")
    tile_title = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//p[contains(text(), 'Test automation project')]")
    ))

    # ✅ STEP 7: Click the parent container of the title (div with role='link')
    tile_parent = tile_title.find_element(By.XPATH, "./ancestor::div[@role='link']")
    print("🧭 Found the tile container, clicking it now...")
    tile_parent.click()
    print("✅ Successfully clicked 'Test automation project' tile.")

except Exception as e:
    # ✅ STEP 8: If anything goes wrong, print the error and take a screenshot for debugging
    print("❌ ERROR during execution:", e)
    driver.save_screenshot("step2_error.png")
    print("🖼️ Screenshot saved as step2_error.png for debugging.")

finally:
    # ✅ STEP 9: Wait for 5 seconds before closing the browser (for visual confirmation)
    time.sleep(5)
    driver.quit()  # Closes the browser and ends the session
