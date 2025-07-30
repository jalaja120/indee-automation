from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# ✅ Step 0: Setup Chrome WebDriver
# Provide the correct path to your ChromeDriver executable
driver_path = "C:\\WebDrivers\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Optional: Open browser in full screen

try:
    # ✅ Step 1: Launch the Indee demo FYC platform
    driver.get("https://indeedemo-fyc.watch.indee.tv/")
    print("🌐 Opened Indee demo page")

    # Create a WebDriverWait object for waiting on elements to load
    wait = WebDriverWait(driver, 20)

    # ✅ Step 2: Wait until the PIN field is available and enter the PIN
    print("🔄 Waiting for the PIN input field...")
    pin_input = wait.until(EC.presence_of_element_located((By.ID, "pin")))
    pin_input.send_keys("WVMVHWBS")
    print("🔐 Entered PIN")

    # ✅ Step 3: Wait until the 'Sign In' button becomes clickable and click it
    print("🔄 Waiting for SIGN IN button to become clickable...")
    sign_in_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Sign In']")  # Adjusted text case
    ))
    sign_in_button.click()
    print("✅ Clicked SIGN IN button")

    # You can now add steps like waiting for the tile, playing video, etc.
    # This just completes login successfully

except Exception as e:
    print("❌ Error during login process:", e)
    # Save screenshot of failure state
    driver.save_screenshot("login_error.png")
    print("🖼️ Screenshot saved as 'login_error.png' for debugging")

finally:
    # Optional delay to observe the result before quitting
    time.sleep(5)
    driver.quit()
    print("🚪 Browser closed")
