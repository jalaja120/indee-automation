# Required imports for Selenium automation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# 🔐 Ask user to input their PIN for login
pin = input("Enter your Indee PIN: ").strip()

# 🌐 Set the login URL of the Indee demo platform
url = "https://indeedemo-fyc.watch.indee.tv/login"

# 📁 Path to the ChromeDriver executable
driver_path = r"C:\WebDrivers\chromedriver-win64\chromedriver.exe"

# 🧰 Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Start browser in maximized mode

# 🚗 Initialize the Chrome browser with options
driver = webdriver.Chrome(service=Service(driver_path), options=options)

# ⏳ Setup WebDriverWait for waiting on elements
wait = WebDriverWait(driver, 10)

try:
    print("🌐 Opening Indee platform...")
    driver.get(url)  # Open the website

    # 🔍 Try logging in if the PIN input field is found
    try:
        print("🔐 Checking if login is required...")
        pin_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "pin"))  # Wait for the PIN input field
        )
        print("🔐 PIN screen detected. Entering PIN...")
        pin_input.send_keys(pin)  # Enter the PIN

        # Click on the "SIGN IN" button
        sign_in_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        sign_in_btn.click()
        print("✅ Signed in.")
    
    except TimeoutException:
        # If PIN screen doesn't show up in 5 seconds, assume already signed in
        print("🔓 Already signed in — skipping login.")

    # 📺 Wait for the presence of the "Test automation project" tile
    print("📺 Waiting for 'All Titles' screen...")
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//h5[contains(text(), 'Test automation project')]")
    ))

    # 🎬 Click on the tile by locating its ancestor div
    print("🎬 Opening 'Test automation project' tile...")
    project_tile = driver.find_element(
        By.XPATH, "//h5[contains(text(), 'Test automation project')]/ancestor::div[@role='link']"
    )
    project_tile.click()

    # ⏳ Wait for the Play button to appear instead of <video> element
    print("⏳ Waiting for video play button...")
    play_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Play')]"))
    )

    # ▶️ Click Play to start the video
    print("▶️ Clicking Play...")
    play_button.click()
    time.sleep(10)  # Let the video play for 10 seconds

    # ⏸️ Try clicking Pause if the button appears
    try:
        pause_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Pause')]"))
        )
        pause_button.click()
        print("⏸️ Video paused.")
    
    except TimeoutException:
        print("⚠️ Pause button not found, skipping pause.")

    print("✅ Step 4 complete.")

# ❌ Catch and handle any unexpected errors during automation
except Exception as e:
    print(f"❌ Error during automation: {e}")
    driver.save_screenshot("step4_continue_error.png")
    print("🖼️ Screenshot saved as step4_continue_error.png")

# 🧹 Cleanup and close the browser
finally:
    time.sleep(2)
    driver.quit()
