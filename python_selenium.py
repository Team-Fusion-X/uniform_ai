from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import json

# driver 셋팅 API
def update_chrome():
    global driver
    
    # 자동 꺼짐 방지 -> vscode에서 개발할 땐 f5말고 run python file로 실행
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True) 
    chrome_options.add_argument('lang=ko_KR')  # 사용언어 한국어
    chrome_options.add_argument('disable-gpu')  # 하드웨어 가속 안함
    #chrome_options.add_argument("headless") # 백그라운드 실행
    chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])  # 불필요한 에러 메세지 삭제 
    driver = webdriver.Chrome(options=chrome_options) # 크롬 드라이버 생성
    driver.implicitly_wait(100) # 페이지 로딩이 완료될 떼까지 기다리는 코드 (10초 설정)
    
    return

def create_json_file(result_data):
    # 폴더명 및 파일명 지정
        output_folder = 'json_data'
        output_file_name = f"2019_pass_or_fail.json_2"
        output_path = os.path.join(os.path.dirname(__file__), output_folder)
    
        # extract_json 폴더가 없으면 생성
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # 추출한 데이터를 JSON 파일로 저장
        output_file = os.path.join(output_path, output_file_name)
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(result_data, json_file, indent=4, ensure_ascii=False)

# driver.find_element_by_xpath(XPATH)
'''
(1,2), (1,3) ~ (1,15)
...
(15,2), (15,3) ~ (15,15)
'''
def search_data():   
    for i in range(1,16):
        area = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[2]').text
        field = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[3]').text
        university = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[4]').text
        department = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[5]').text
        college_admissions_field = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[6]').text
        college_admissions_name = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[7]').text
        minimum_score_necessity = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[8]').text
        result_initial = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[9]').text
        result_total = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[10]').text
        all_average = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[11]').text
        kemso_average = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[12]').text
        kemsi_average = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[13]').text
        keme_percentile = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[14]').text
        keme_rating = driver.find_element(By.XPATH, f'//*[@id="list_area"]/div/table/tbody/tr[{i}]/td[15]').text

        data = {
                    "지역": area,
                    "계열": field,
                    "대학명": university,
                    "학과명": department,
                    "전형유형": college_admissions_field,
                    "전형명": college_admissions_name,
                    "최저적용유무": minimum_score_necessity,
                    "최초지원결과": result_initial,
                    "최종지원결과": result_total,
                    "전과목(평균)": all_average,
                    "국영수사(평균)": kemso_average,
                    "국영수과(평균)": kemsi_average,
                    "국영수탐(백분위)": keme_percentile,
                    "국영수탐(등급)": keme_rating
                }
        
        result_data.append(data)


# 다음 페이지 매개변수 -> 페이지 4~13
def next_page(index):
    # 다음 페이지
    driver.find_element(By.XPATH, f'//*[@id="list_area"]/ul/li[{index}]/a').click()
    driver.implicitly_wait(100)

  
# url을 매개변수로 페이지 오픈 API
def open_page(page_url):
    driver.get(page_url)
    driver.implicitly_wait(100)
    return
   
if __name__ == "__main__":
    result_data = []
    update_chrome()
    # 사이트 접속
    open_page('https://ipsi.jinhak.or.kr/subList/20000000095')
    
    while 1:
        try:
            for i in range(4,14):
                search_data()
                next_page(i)
                
        except:
            driver.quit()
            create_json_file(result_data)