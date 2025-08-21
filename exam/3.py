import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 웹브라우저 설치, 옵션
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=Options())
# 로그인 페이지 접속
driver.get("https://www.saucedemo.com/")
# TODO: 로그인 시작
# 아이디
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
# 암호
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
# 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

# 시간지연 : 1초
time.sleep(1)

# 로그인 후 첫 페이지에서 상품 설명 가져오기
t = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_desc")

# t: 상품 설명 배열
for i in range(len(t)):
    print(t[i].text)

driver.quit()

