from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to your ChromeDriver
CHROMEDRIVER_PATH = "C:/WebDrivers/chromedriver-win64/chromedriver.exe"

# Chrome options
options = Options()
options.add_experimental_option("detach", True)  # Keeps browser open after script ends (optional)

# Set up driver with the correct service
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Now use driver as usual
driver.get("https://indeedemo-fyc.watch.indee.tv/")
