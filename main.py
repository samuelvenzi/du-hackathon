from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import time
import os

def search_and_save_images(query, num_images):
    driver = webdriver.Chrome()  # You'll need to have Chrome and chromedriver installed

    url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
    driver.get(url)

    # Simulate scrolling to load more images
    for _ in range(num_images // 20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    os.makedirs(query, exist_ok=True)

    # Find and save the image links
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img.Q4LuWd')
    for i, element in enumerate(image_elements[:num_images]):
        element.click()
        time.sleep(1)
        img = driver.find_element(By.CSS_SELECTOR, 'img.sFlh5c.pT0Scc.iPVvYb')
        src = img.get_attribute('src')
        print(src)
        if src:
            response = requests.get(src)
            with open(f"{query}/image_{i+1}.jpg", "wb") as f:
                f.write(response.content)

    driver.quit()

if __name__ == "__main__":
    search_and_save_images('early tar spot corn "leaf"', 100)
