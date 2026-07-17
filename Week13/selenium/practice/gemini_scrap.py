from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from webdriver_manager.core.os_manager import ChromeType

# Or pin explicitly:

opt = Options()
opt.add_argument("--disable-gpu")
opt.add_argument("--window-size=1920,1080")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")

# Profile setup
opt.add_argument(r"--user-data-dir=C:\Users\keval\AppData\Local\Google\Chrome\User Data")
opt.add_argument(r"--profile-directory=Default")

# Prevent Chrome from blocking automation
opt.add_experimental_option("excludeSwitches", ["enable-automation"])
opt.add_experimental_option("useAutomationExtension", False)

# Remove remote debugging port — often causes conflicts
# opt.add_argument("--remote-debugging-port=9222")  # <-- remove this

service = Service(ChromeDriverManager(driver_version="148.0.7778.168").install())
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opt)

driver.get("https://gemini.google.com/")
print(driver.title)