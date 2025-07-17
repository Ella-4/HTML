from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service('/opt/homebrew/bin/geckodriver')
driver = webdriver.Firefox(service=service)

# 이후 코드...

# 지시사항 1번
with webdriver.Firefox() as driver:
    # 지시사항 2번
    driver.get("http://localhost:8080")

    # 지시사항 3번
    t = driver.find_element(By.TAG_NAME, "title")
    print(t.text)

    # 지시사항 4번
    imgs = driver.find_elements(By.TAG_NAME, "img")
    for img in imgs:
        print(img.get_attribute("src"))

    # 지시사항 5번
    divs = driver.find_elements(By.TAG_NAME, "div")
    for div in divs:
        ps = div.find_elements(By.TAG_NAME, "p")
        for p in ps:
            print(p.text)
