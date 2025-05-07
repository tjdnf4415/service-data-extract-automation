import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. 엑셀에서 i열 데이터 읽기
#df = pd.read_excel('your_file.xlsx')
#search_values = df['I'].tolist()  # 'I' 컬럼명에 맞게 수정
search_values = ["A50045680"]

# 2. 셀레니움 크롬 드라이버 실행
driver = webdriver.Chrome()  # chromedriver가 PATH에 있어야 함

results = []

# a서비스 로그인 페이지로 이동
driver.get('https://mas.lgcaremall.com:8000/login')  # 실제 로그인 URL로 변경

time.sleep(1)  # 페이지 로딩 대기

# 아이디 입력
admin_id_input = driver.find_element(By.NAME, 'adminId')
admin_id_input.clear()
admin_id_input.send_keys('exusgroup24')  # 실제 아이디로 변경

# 비밀번호 입력
password_input = driver.find_element(By.ID, 'password')
password_input.clear()
password_input.send_keys('icebrown15!')  # 실제 비밀번호로 변경

# 로그인 버튼 클릭 (예시: 버튼이 <button type="submit">로그인</button> 인 경우)
login_button = driver.find_element(By.ID, 'btnLogin')
login_button.click()

time.sleep(2)

for value in search_values:
    driver.get('https://mas.lgcaremall.com:8000/product/list')  # a서비스 주소로 이동
    time.sleep(1)  # 페이지 로딩 대기

    # 검색 input에 값 입력 (id값은 실제로 확인 필요)
    search_input = driver.find_element(By.ID, 'productValue')
    search_input.clear()
    search_input.send_keys(value)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)  # 검색 결과 대기

    # (1) 첫 번째 요소 클릭 (예: 버튼, 탭 등)
    first_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'form?productId=')
    first_element.click()
    time.sleep(0.5)  # 클릭 후 잠깐 대기

    # (2) 두 번째 요소 클릭
    second_element = driver.find_element(By.PARTIAL_LINK_TEXT, '/product/material/list?supplier')
    second_element.click()
    time.sleep(0.5)  # 클릭 후 잠깐 대기

    # (3) 세 번째 요소 클릭
    third_element = driver.find_element(By.PARTIAL_LINK_TEXT, 'form?supplier')
    third_element.click()
    time.sleep(0.5)  # 클릭 후 잠깐 대기

    # 모든 textarea 요소를 리스트로 가져오기
    textareas = driver.find_elements(By.TAG_NAME, 'textarea')

    # 각 textarea의 값을 추출해서 리스트로 저장
    values = [textarea.get_attribute('value') for textarea in textareas]

    first_five = values[:11]
    results.append(first_five)

    # (4) 결과 input에서 값 추출
    # result_input = driver.find_element(By.ID, '결과input의id')
    # result_value = result_input.get_attribute('value')
    # results.append(result_value)

driver.quit()

# 3. 결과를 엑셀로 저장
# df['결과'] = results
# df.to_excel('결과저장.xlsx', index=False)
