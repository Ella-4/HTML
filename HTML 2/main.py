from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# 지시사항 1번: Firefox 브라우저를 with 문으로 실행 (자동 종료 보장)
service = Service('/opt/homebrew/bin/geckodriver')
with webdriver.Firefox(service=service) as driver:

    # 지시사항 2번: 로컬 서버에 접속 (index.html 페이지가 띄워짐)
    driver.get("http://localhost:8080")

    # 지시사항 3번: <title> 태그 요소를 찾아서 그 텍스트 출력
    t = driver.find_element(By.TAG_NAME, "title")
    print("title:", t.text)

    # 지시사항 4번: 모든 <img> 태그 요소를 찾아서 각 src 속성 출력
    imgs = driver.find_elements(By.TAG_NAME, "img")
    for img in imgs:
        print("img src:", img.get_attribute("src"))

    # 지시사항 5번: 모든 <div> 요소 안에 포함된 모든 <p> 요소를 찾아서 텍스트 출력
    divs = driver.find_elements(By.TAG_NAME, "div")
    for div in divs:
        ps = div.find_elements(By.TAG_NAME, "p")
        for p in ps:
            print("p text:", p.text)

    # ~ 지시사항이 아니지만, 브라우저를 계속 열어두고 싶을 때
    # 사용자로부터 'exit' 입력을 받으면 브라우저를 종료하도록 할 수 있습니다.
    while True:
        command = input("브라우저를 종료하려면 'exit'를 입력하세요: ")
        if command.lower() == "exit":
            print("브라우저를 종료합니다.")
            break
