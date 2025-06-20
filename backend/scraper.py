from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse

BASE_URL = "https://creerinfotech.com"
OUTPUT_FILE = "full_website_content-3.txt"

options = Options()
options.add_argument("--headless") 
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

to_visit = [BASE_URL]
visited = set()
final_text = ""

def is_internal(url):
    return url and BASE_URL in urlparse(url).geturl()

def clean(u):
    return u.split("#")[0].rstrip("/")

while to_visit:
    url = to_visit.pop(0)
    url = clean(url)
    if url in visited:
        continue
    visited.add(url)

    print(f"🔗 Visiting: {url}")
    driver.get(url)
    time.sleep(2)

    # Scroll entirely
    while True:
        last = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if driver.execute_script("return document.body.scrollHeight") == last:
            break
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Extract text
    text = soup.get_text(separator="\n", strip=True)
    final_text += f"{text}\n"

    # Collect new internal links in visual order
    for a in driver.find_elements(By.TAG_NAME, "a"):
        href = a.get_attribute("href")
        if href and is_internal(href):
            link = clean(href)
            if link not in visited and link not in to_visit:
                to_visit.append(link)


driver.quit()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(final_text)

print(f"\n Scraped {len(visited)} pages into '{OUTPUT_FILE}'")
