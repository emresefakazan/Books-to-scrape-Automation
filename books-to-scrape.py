#Books to scrape sayfasını selenium ile next butonuna tıklayarak scrape ettik.


import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

# 🔹 Chrome'u başlat
driver = uc.Chrome()
driver.get("http://books.toscrape.com/")
driver.maximize_window()
time.sleep(2)

while True:
    # 1️⃣ Sayfa HTML'sini çek
    soup = BeautifulSoup(driver.page_source, "lxml")

    # 2️⃣ Kitapları çek
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        print(title, "|", price)

    print("-" * 60)

    # 3️⃣ “Next” butonunu bul ve tıkla
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "next")
        print("➡ Sonraki sayfaya geçiliyor...")
        next_button.click()
        time.sleep(2)  # Sayfanın yüklenmesini bekle
    except:
        print("✅ Son sayfaya ulaşıldı.")
        break

driver.quit()
