from selenium import webdriver
from selenium.webdriver.common.by import By  # Importing strategies to locate elements (e.g., By.ID, By.XPATH)
from selenium.webdriver.support.ui import WebDriverWait  # To wait for certain conditions like presence of elements
from selenium.webdriver.support import expected_conditions as EC  # Provides expected conditions to wait on
from selenium.webdriver.chrome.service import Service  # To set the ChromeDriver path for Selenium
import time  # Used for hardcoded wait/sleep durations

# ✅ Setup: ChromeDriver path to control the browser
driver_path = "C:\\WebDrivers\\chromedriver-win64\\chromedriver.exe"  # Replace with actual path on your machine
service = Service(executable_path=driver_path)

# ✅ Start a new Chrome browser session
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Optional: Makes the browser window full screen

try:
    wait = WebDriverWait(driver, 20)  # Set maximum timeout of 20 seconds for all wait operations

    # ✅ Step 1: Open Indee FYC demo platform and log in using PIN
    print("🌐 Opening Indee platform...")
    driver.get("https://indeedemo-fyc.watch.indee.tv/")

    print("🔐 Entering PIN...")
    pin_input = wait.until(EC.presence_of_element_located((By.ID, "pin")))  # Wait for PIN input field to be available
    pin_input.send_keys("WVMVHWBS")  # Simulate user typing the PIN

    sign_in_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'SIGN IN')]")  # Locate the "SIGN IN" button using partial text
    ))
    sign_in_button.click()  # Click the "SIGN IN" button
    print("✅ Logged in successfully.")

    # ✅ Step 2: Click on the video tile titled "Test automation project"
    print("🎬 Locating 'Test automation project' tile...")
    tile = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='link' and contains(@title, 'Test automation project')]")  # Locate video tile
    ))
    tile.click()  # Simulate user clicking the video
    print("✅ Clicked on 'Test automation project' tile.")
    
    # ✅ Step 3: Wait for the player to load completely
    print("⏳ Waiting for video player to load...")
    time.sleep(5)  # Allowing time for video page to fully render

    # ✅ Step 4: Locate and click the Play button
    print("▶️ Looking for the play button...")
    play_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button.vjs-play-control")  # Class for video.js play button
    ))
    play_button.click()  # Start playing the video
    print("🎥 Video started playing...")

    time.sleep(10)  # Simulate user watching the video for 10 seconds

    play_button.click()  # Pause the video
    print("⏸️ Video paused after 10 seconds.")

except Exception as e:
    # ✅ In case any step fails, log the error and capture screenshot
    print("❌ ERROR during execution:", e)
    driver.save_screenshot("step3_error.png")  # Screenshot saved in the current working directory
    print("🖼️ Screenshot saved as step3_error.png for review.")

finally:
    # ✅ Final cleanup step to close the browser
    time.sleep(5)  # Wait for visual confirmation before closing
    driver.quit()  # Gracefully end the session and close browser
