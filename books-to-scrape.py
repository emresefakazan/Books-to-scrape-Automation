import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# 🔹 Launch Chrome browser
driver = uc.Chrome()
driver.get("http://books.toscrape.com/")
driver.maximize_window()
time.sleep(2)

while True:
    # 1️⃣ Parse the current page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "lxml")

    # 2️⃣ Extract all book items on the page
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        print(title, "|", price)

    print("-" * 60)

    # 3️⃣ Find and click the "Next" button to go to the next page
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "next")
        print("➡ Moving to the next page...")
        next_button.click()
        time.sleep(2)  # Wait for the page to load
    except:
        print("✅ Reached the last page.")
        break

driver.quit()
