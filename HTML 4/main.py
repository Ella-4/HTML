from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service('/opt/homebrew/bin/geckodriver')  # geckodriver 경로

# 1번: Firefox 실행
with webdriver.Firefox(service=service) as driver:
    # 2번: 로컬 서버 접속
    driver.get("http://localhost:8080")

    # 3번: <ol> 내부 모든 <li> 출력
    xpath = '/html/body/ol/li'
    li_list = driver.find_elements(By.XPATH, xpath)
    print("ol/li:")
    for li in li_list:
        print(li.text)

    # 4~5번: class에 'big' 포함된 요소들 출력
    xpath2 = "//*[contains(@class, 'big')]"
    big_list = driver.find_elements(By.XPATH, xpath2)
    print("\nclass='big':")
    for big in big_list:
        print(big.text)

    # 6~7번: class에 'bold' 포함된 요소들 출력
    xpath3 = "//*[contains(@class, 'bold')]"
    bold_list = driver.find_elements(By.XPATH, xpath3)
    print("\nclass='bold':")
    for bold in bold_list:
        print(bold.text)

    # 종료 대기
    input("\n종료하려면 'exit' 입력: ")
