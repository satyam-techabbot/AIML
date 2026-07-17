# Selenium

## What is Selenium?
Selenium is an open-source automation framework used to automate web browsers. It is mainly used for:
* Web application testing
* Repetitive browser tasks
* Scraping and automation workflows
* Cross-browser testing

Supported browsers:
* Chrome
* Firefox
* Edge
* Safari

Supported languages:
* Java
* Python
* C#
* JavaScript
* Ruby

Official website: [Selenium](https://www.selenium.dev)

---

# Selenium Components

## 1. Selenium WebDriver

Main component used to automate browser actions.

Example actions:
* Open website
* Click buttons
* Enter text
* Validate content

---

## 2. Selenium IDE

Selenium IDE is a browser extension for record-and-playback testing.

Good for beginners.

---

## 3. Selenium Grid

Selenium Grid allows running tests on multiple machines and browsers simultaneously.

Used for:
* Parallel execution
* Cross-browser testing
* Faster execution

---

# Selenium Architecture

```text
Test Script
    ↓
WebDriver API
    ↓
Browser Driver
    ↓
Real Browser
```

Example:
* Chrome → ChromeDriver
* Firefox → GeckoDriver

---

# Installation (Python)

## Install Selenium
```bash
pip install selenium
```

## Install Browser Driver

### ChromeDriver

Download from:
[Chrome for Testing Drivers](https://googlechromelabs.github.io/chrome-for-testing/?utm_source=chatgpt.com)

OR use automatic driver management:
```bash
pip install webdriver-manager
```

---

# First Selenium Program (Python)

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print(driver.title)

driver.quit()
```

---

# Important WebDriver Methods

| Method        | Description       |
| ------------- | ----------------- |
| `get(url)`    | Open website      |
| `title`       | Get page title    |
| `current_url` | Current URL       |
| `back()`      | Browser back      |
| `forward()`   | Browser forward   |
| `refresh()`   | Refresh page      |
| `close()`     | Close current tab |
| `quit()`      | Close browser     |

---

# Locators in Selenium

Locators identify web elements.

## Common Locators

| Locator      | Example           |
| ------------ | ----------------- |
| ID           | `By.ID`           |
| Name         | `By.NAME`         |
| Class Name   | `By.CLASS_NAME`   |
| Tag Name     | `By.TAG_NAME`     |
| XPath        | `By.XPATH`        |
| CSS Selector | `By.CSS_SELECTOR` |

---

# Example: Finding Elements

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

element = driver.find_element(By.ID, "username")

element.send_keys("admin")
```

---

# XPath Basics

## Absolute XPath

```xpath
/html/body/div/input
```

Not recommended.

## Relative XPath

```xpath
//input[@id='username']
```

Preferred approach.

## Common XPath Functions

| XPath           | Meaning           |
| --------------- | ----------------- |
| `//tagname`     | Select tag        |
| `contains()`    | Partial match     |
| `text()`        | Match text        |
| `starts-with()` | Starts with value |

Example:

```xpath
//button[contains(text(),'Login')]
```

---

# CSS Selector Examples

```css
#username
```

```css
input[type='text']
```

```css
button.login-btn
```

---

# Waits in Selenium

## 1. Implicit Wait

```python
driver.implicitly_wait(10)
```

Waits globally.

---

## 2. Explicit Wait

Preferred method.

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)
```

---

# Handling Alerts

```python
alert = driver.switch_to.alert

alert.accept()
```

Other methods:

* `dismiss()`
* `text`
* `send_keys()`

---

# Handling Dropdowns

```python
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "country"))

dropdown.select_by_visible_text("India")
```

---

# Handling Frames

```python
driver.switch_to.frame("frameName")
```

Return to main page:

```python
driver.switch_to.default_content()
```

---

# Window Handling

```python
driver.window_handles
```

Switch window:

```python
driver.switch_to.window(handle)
```

---

# Mouse Actions

Using ActionChains:

```python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)

actions.move_to_element(element).perform()
```

Common actions:

* Hover
* Double click
* Right click
* Drag and drop

---

# Keyboard Actions

```python
from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.ENTER)
```

---

# Taking Screenshot

```python
driver.save_screenshot("image.png")
```

---

# Executing JavaScript

```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

---

# Headless Browser

Runs browser without GUI.

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
```

---

# PyTest with Selenium

Install:

```bash
pip install pytest
```

Official website: [pytest documentation](https://docs.pytest.org?utm_source=chatgpt.com)

Example:

```python
def test_google_title():
    driver = webdriver.Chrome()

    driver.get("https://google.com")

    assert "Google" in driver.title

    driver.quit()
```

Run tests:

```bash
pytest
```

---

# Page Object Model (POM)

Design pattern used in Selenium automation.

Benefits:

* Reusable code
* Easy maintenance
* Better structure

Structure example:

```text
pages/
tests/
utils/
```

---

# Common Selenium Exceptions

| Exception                       | Reason                  |
| ------------------------------- | ----------------------- |
| NoSuchElementException          | Element not found       |
| TimeoutException                | Wait timeout            |
| StaleElementReferenceException  | DOM updated             |
| ElementNotInteractableException | Element disabled/hidden |

---

# Best Practices

* Prefer Explicit Waits
* Use stable locators
* Avoid hardcoded sleep
* Use Page Object Model
* Keep tests independent
* Capture screenshots on failure

---

# Selenium Interview Questions

## Q1. Difference between close() and quit()

* `close()` → closes current tab
* `quit()` → closes entire browser session

---

## Q2. Implicit vs Explicit Wait

* Implicit → global wait
* Explicit → wait for specific condition

---

## Q3. Why is XPath used?

Used when:
* ID not available
* Dynamic elements
* Complex DOM traversal

---

# Advanced Topics
* Data-driven testing
* Parallel execution
* Docker with Selenium
* CI/CD integration
* Jenkins integration
* Selenium Grid
* Allure reports

---

# Useful Resources
* [Selenium Documentation](https://www.selenium.dev/documentation/)
* [Selenium Python Docs](https://selenium-python.readthedocs.io/)
* [PyTest Documentation](https://docs.pytest.org)
* [Chrome for Testing Drivers](https://googlechromelabs.github.io/chrome-for-testing/)
