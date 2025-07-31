from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service)
driver.get('https://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000166')
time.sleep(1)


# 1. '행정구역별' 선택 클릭
driver.find_element(By.ID, 'area2').click()
time.sleep(1)

# 2. 전체선택 체크박스 해제
check_all = driver.find_element(By.ID, 'checkAll')
if check_all.is_selected():
    check_all.click()
    time.sleep(0.5)

# 3. 주택용 체크박스 선택
housing_checkbox = driver.find_element(By.ID, 'cbCntr1')
if not housing_checkbox.is_selected():
    housing_checkbox.click()
    time.sleep(0.5)

# 4. 시도 목록 불러오기
sido_select = Select(driver.find_element(By.ID, 'searchSiDo'))
time.sleep(1)

# '전체' 시도 제외하고 실제 시도만 가져오기
sido_list = [
    option.get_attribute('value') 
    for option in sido_select.options 
    if option.get_attribute('value') != "전체"
]

results = []

for sido in sido_list:
    # 시도 선택
    Select(driver.find_element(By.ID, 'searchSiDo')).select_by_value(sido)
    time.sleep(1)

    for year in range(2020, 2025):  # 테스트 완료 후 변경
        for month in ['06', '07', '08']:
            # 연도/월 선택
            Select(driver.find_element(By.ID, 'sdateYear')).select_by_value(str(year))
            Select(driver.find_element(By.ID, 'sdateMonth')).select_by_value(month)
            Select(driver.find_element(By.ID, 'edateYear')).select_by_value(str(year))
            Select(driver.find_element(By.ID, 'edateMonth')).select_by_value(month)
            time.sleep(0.5)

            # 조회 버튼 클릭
            driver.find_element(By.ID, 'btn_search').click()
            time.sleep(2)

            # 테이블 파싱
            try:
                table = driver.find_element(By.ID, 'table_des')
                tbody = table.find_element(By.TAG_NAME, 'tbody')
                rows = tbody.find_elements(By.TAG_NAME, 'tr')

                for tr in rows:
                    cols = tr.find_elements(By.TAG_NAME, 'td')
                    if len(cols) >= 6:
                        region = cols[0].text.strip()
                        contract_type = cols[1].text.strip()

                        # '전체' 지역 + '주택용' 계약만 필터링
                        if region == '전체' and contract_type == '주택용':
                            usage = cols[3].text.replace(',', '').strip()
                            bill = cols[4].text.replace(',', '').strip()
                            unit_price = cols[5].text.replace(',', '').strip()
                            results.append({
                                '시도': sido,
                                '연도': year,
                                '월': month,
                                '사용량(kWh)': usage,
                                '전기요금(원)': bill,
                                '평균단가(원/kWh)': unit_price
                            })
                            print(f"[추출됨] {region}-{contract_type}: {[td.text for td in cols]}")
                        else:
                            print(f"[필터됨] {region}-{contract_type}: {[td.text for td in cols]}")

            except Exception as e:
                print(f"[{sido}-{year}-{month}] 테이블 추출 실패: {e}")
                continue

# 결과 저장
df = pd.DataFrame(results)
df.to_csv("주택용_전력데이터.csv", index=False, encoding='utf-8-sig')

driver.quit()