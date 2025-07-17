from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service = Service('/opt/homebrew/bin/geckodriver')  # 경로는 설치 위치에 맞게 수정

# 지시사항 1번: Firefox 브라우저를 with 문으로 실행
with webdriver.Firefox(service=service) as driver:
    # 지시사항 2번: 로컬 서버 접속
    driver.get("http://localhost:8080")

    # 지시사항 3번: <ol> 요소 안의 모든 <li> 텍스트 출력
    o = driver.find_element(By.TAG_NAME, "ol")
    l = o.find_elements(By.TAG_NAME, "li")
    for li in l:
        print(li.text)

    # 지시사항 4번: class가 'big'인 요소 모두 출력 (ul 내의)
    ul = driver.find_element(By.TAG_NAME, "ul")
    big_list = ul.find_elements(By.CLASS_NAME, "big")
    for big in big_list:
        print(big.text)

    # 지시사항 5번: class가 'bold'인 요소 모두 출력 (ul 내의)
    bold_list = ul.find_elements(By.CLASS_NAME, "bold")
    for bold in bold_list:
        print(bold.text)

    # ~ 사용자가 'exit' 입력하면 종료합니다. (이건 지시사항이 아닙니다)
    while True:
        cmd = input("종료하려면 'exit'를 입력하세요: ")
        if cmd.strip().lower() == "exit":
            break
