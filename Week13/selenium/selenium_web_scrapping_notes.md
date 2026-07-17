# Selenium Notes for Web Scraping

## What is Selenium for Web Scraping?

Selenium can automate browsers to scrape data from websites that use:
* JavaScript rendering
* Infinite scrolling
* Dynamic content
* Login systems
* AJAX requests

Unlike simple scraping libraries like `requests`, Selenium interacts with a real browser.

Official Docs: [Selenium Documentation](https://www.selenium.dev/documentation/)

---

# Installation

## Install Selenium
```bash
pip install selenium
```

## Install WebDriver Manager
```bash
pip install webdriver-manager
```

---

# First Scraping Program

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://example.com")

print(driver.title)

driver.quit()
```

---

# Running Browser in Headless Mode

Headless mode runs without opening browser UI.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
```

Benefits:

* Faster scraping
* Saves memory
* Good for servers/cloud

---

# Finding Elements

## Import By
```python
from selenium.webdriver.common.by import By
```

---

# Locators
| Locator      | Example           |
| ------------ | ----------------- |
| ID           | `By.ID`           |
| Class        | `By.CLASS_NAME`   |
| XPath        | `By.XPATH`        |
| CSS Selector | `By.CSS_SELECTOR` |
| Tag          | `By.TAG_NAME`     |

---

# Scraping Text

```python
title = driver.find_element(By.TAG_NAME, "h1")

print(title.text)
```

---

# Scraping Multiple Elements

```python
products = driver.find_elements(By.CLASS_NAME, "product")

for product in products:
    print(product.text)
```

---

# Scraping Links

```python
link = driver.find_element(By.TAG_NAME, "a")

print(link.get_attribute("href"))
```

---

# Scraping Images

```python
img = driver.find_element(By.TAG_NAME, "img")

print(img.get_attribute("src"))
```

---

# XPath for Scraping

## Basic XPath

```xpath
//div
```

## Attribute XPath

```xpath
//input[@type='text']
```

## Contains

```xpath
//button[contains(text(),'Login')]
```

## Starts-With

```xpath
//div[starts-with(@class,'card')]
```

---

# CSS Selectors for Scraping

```css
.product
```

```css
#main
```

```css
div.card h2
```

---

# Waiting for Dynamic Content

## Explicit Wait (Important)

Most important concept in scraping.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "product"))
)
```

---

# Infinite Scroll Scraping

Many sites load content while scrolling.

```python
import time

last_height = driver.execute_script(
    "return document.body.scrollHeight"
)

while True:
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)

    new_height = driver.execute_script(
        "return document.body.scrollHeight"
    )

    if new_height == last_height:
        break

    last_height = new_height
```

---

# Clicking "Load More" Button

```python
button = driver.find_element(By.ID, "load-more")

button.click()
```

With loop:

```python
while True:
    try:
        button = driver.find_element(By.ID, "load-more")
        button.click()
    except:
        break
```

---

# Handling Login Pages

```python
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("myusername")
password.send_keys("mypassword")

login_btn = driver.find_element(By.ID, "login")

login_btn.click()
```

---

# Saving Cookies

```python
cookies = driver.get_cookies()

print(cookies)
```

---

# Using User-Agent

```python
options.add_argument(
    "user-agent=Mozilla/5.0"
)
```

---

# Disable Automation Detection

Some websites block bots.

```python
options.add_argument("--disable-blink-features=AutomationControlled")
```

---

# Taking Screenshot While Scraping

```python
driver.save_screenshot("page.png")
```

Useful for debugging.

---

# Extracting Table Data

```python
rows = driver.find_elements(By.TAG_NAME, "tr")

for row in rows:
    print(row.text)
```

---

# Extracting Data into List

```python
data = []

items = driver.find_elements(By.CLASS_NAME, "product")

for item in items:
    data.append(item.text)

print(data)
```

---

# Saving Data to CSV

```python
import csv

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name"])

    for item in data:
        writer.writerow([item])
```

---

# Scraping Example (Quotes Website)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com")

quotes = driver.find_elements(By.CLASS_NAME, "quote")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text

    author = quote.find_element(By.CLASS_NAME, "author").text

    print(text, "-", author)

driver.quit()
```

---

# Common Exceptions

| Exception                        | Meaning           |
| -------------------------------- | ----------------- |
| NoSuchElementException           | Element not found |
| TimeoutException                 | Wait timeout      |
| StaleElementReferenceException   | Page updated      |
| ElementClickInterceptedException | Element blocked   |

---

# Best Practices

## Use Explicit Waits

Better than `time.sleep()`.

---

## Avoid Too Many Requests

Add delays:

```python
import time

time.sleep(2)
```

---

## Rotate User Agents

Prevents detection.

---

## Respect robots.txt

Check website scraping rules.

---

## Avoid Scraping Restricted Data

Do not scrape:
* Personal data
* Private accounts
* Protected content

---

# Selenium vs BeautifulSoup

| Selenium           | BeautifulSoup   |
| ------------------ | --------------- |
| Handles JavaScript | No JS support   |
| Slower             | Faster          |
| Real browser       | HTML parser     |
| Dynamic websites   | Static websites |

Best practice:

* Use Selenium to load page
* Use BeautifulSoup to parse HTML

Example:
```python
from bs4 import BeautifulSoup

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
```

Official Docs:

* [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

---

# Advanced Selenium Scraping

## Scraping with Proxy

```python
options.add_argument("--proxy-server=http://proxy:port")
```

---

## Mobile Emulation

```python
mobile_emulation = {
    "deviceName": "iPhone X"
}

options.add_experimental_option(
    "mobileEmulation",
    mobile_emulation
)
```

---

## Execute JavaScript

```python
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)
```

---

# Useful Libraries with Selenium
| Library        | Purpose            |
| -------------- | ------------------ |
| pandas         | Data analysis      |
| BeautifulSoup  | HTML parsing       |
| requests       | API requests       |
| fake-useragent | Random user agents |

Install:

```bash
pip install pandas beautifulsoup4 fake-useragent
```

---

# Project Ideas
1. Amazon product scraper
2. LinkedIn job scraper
3. News headline scraper
4. Instagram post scraper
5. Flipkart price tracker
6. YouTube comments scraper

---

# Important Notes
* Some websites block Selenium
* CAPTCHA may appear
* Use delays and waits
* APIs are often better than scraping
* Always check Terms of Service

---

# Useful Resources

* [Selenium Documentation](https://www.selenium.dev/documentation/)
* [Selenium Python Docs](https://selenium-python.readthedocs.io/)
* [Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [webdriver-manager](https://pypi.org/project/webdriver-manager/)
