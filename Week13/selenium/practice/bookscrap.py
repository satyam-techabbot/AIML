import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Chrome options
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument("--window-size=1920,1080")

# Driver setup
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(
    service=service,
    options=opt
)

driver.get("https://books.toscrape.com/")
print(driver.title)

page_counter = 1

def navigate_to_next_page():
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, ".next a")
        next_button.click()
        time.sleep(1)
        return True
    except NoSuchElementException:
        return False

def scrap_n_store_in_csv(no_of_pages=10):
    global page_counter

    with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "price"])

        while page_counter <= no_of_pages:

            print(f"Scraping Page {page_counter}")

            books_title = driver.find_elements(
                By.CSS_SELECTOR,
                ".product_pod h3 a"
            )

            books_price = driver.find_elements(
                By.CSS_SELECTOR,
                ".product_price .price_color"
            )

            for title, price in zip(books_title, books_price):
                writer.writerow([
                    title.get_attribute("title"),
                    price.text[1:]
                ])

            page_counter += 1

            if not navigate_to_next_page():
                break

scrap_n_store_in_csv(5)

driver.quit()

print("CSV file 'books.csv' created successfully.")