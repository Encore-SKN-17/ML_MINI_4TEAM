**SK네트웍스 Family AI 캠프 17기 Machine Learning 미니 프로젝트**

---

# 팀 소개

### ✨4조 Dataforce✨

👥 팀 멤버 (개인 GitHub)

| 이름  | GitHub 계정                                    |
| ----- | ---------------------------------------------- |
| 이가은 | [@Leegaeune](https://github.com/Leegaeune)    |
| 이민영 | [@mylee99125](https://github.com/mylee99125) |
| 조해리 | [@Haer111](https://github.com/Haer111)     |
| 주수빈 | [@Subin-Ju](https://github.com/Subin-Ju) |

---

## 💡프로젝트 명

### 지역별 날씨 데이터 기반 냉방 전력 사용량 예측



## ❓프로젝트 소개



---

## ✅ 데이터 출처 목록

| 데이터 이름                           | 파일 형식 / 수집 방법 | 출처 URL |
|--------------------------------------|------------------------|----------|
| 종관기상관측(ASOS) - 자료      |  CSV  / 직접 다운로드  | [바로가기](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36) |
| 주택용 전력 데이터 - 자료      | CSV / 크롤링 통한 다운로드  | [원본 데이터](https://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000166&pstate=L&redirect=Y)|

---

# 🛠️ 기술 스택

| 활용 용도             | 사용한 기술 스택             |
|-----------------------|--------------------------------------|
| 코드 작성              | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Jupyter_Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white"> |
| 군집화                 | <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/Scikit-learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>|
| 시각화                 | <img src="https://img.shields.io/badge/Matplotlib-CB3B27?style=for-the-badge&logo=matplotlib&logoColor=white"> <img src="https://img.shields.io/badge/Seaborn-98FB98?style=for-the-badge&logo=seaborn&logoColor=white">|
| 파일 공유 및 커뮤니케이션| <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">|
  
---

# 🖥️ 데이터 전처리 과정
* **전기 데이터 크롤링 및 컬럼명 처리**
    * `행정구역별` 선택 → `주택용` 체크박스만 선택
    * 시도 목록 불러오기 → 전체 시도 제외, `실제 시도`만 선택
    * `전체` 지역 + `주택용` 계약만 필터링
    * 결과 CSV 파일로 저장
    * CSV 파일 속 시도 코드 - 시도명 매핑 → 저장된 CSV 파일에 `시도명` 컬럼 추가

* **날씨 데이터 csv 파일 로드 및 컬럼명 처리**
    * 최근 5년(2020~2024)의 기상 데이터를 `pandas`를 사용하여 불러옴.
    * `일시`, `평균기온(°C)` 등 원본 컬럼명을 `날짜`, `평균기온` 등으로 일관되게 변경

* **날씨 데이터 형식 변환 및 결측치 처리**
    * `날짜` 컬럼은 `datetime` 형식으로 시간 기반 분석이 가능하도록 변환
    * `평균 기온`, `최고 기온`, `습도` 컬럼은 `to_numeric` 코드를 통해 숫자형 데이터로 변환

* **지역 재그룹핑**
    * 기상 데이터 관측의 기준이 되는 지점이 `시/도` 구분이 아닌 다른 기준으로 세분화 되어 있었음.
    * 세분화된 지점을 `지역`('강원도', '경기', '경남', '경북','광역시 및 특별시', '전남', '전북', 제주', '충남', '충북')으로 재그룹핑.
    * `지역` 컬럼 추가
    * 이후 관측 기준이 되는 지점과 지점명을 (`.drop()`) 코드를 통해 삭제 → '지역' 컬럼을 맨 앞으로 분류
 
* **필요 연월만 남기기**
    * `날짜` 컬럼에서 `연도`와 `월` 분리
    * 분리 후 필요한 달 (6, 7, 8월) 데이터만 추출

* **전기 데이터 + 날씨 데이터 병합**
    * 전기 데이터 속 `지역 코드`와 날씨 데이터 속 `시도명` 매핑
    * `merge` 통해 두 데이터 프레임 병합


---

# 📑 지역별 여름철 전력 사용량 추이 분석
## 1. 지역별 기후 클러스터링
* **클러스터링 과정**
    1. 지역 + 연도별 평균 집계: `agg_features`로 특징 잡기 → `지역`으로 `.groupby` 진행 → `.mean`으로 평균 기온/최저 기온/최고 기온/강수량/풍속/습도/적설량 평균치 계산
    2. 정규화 : `StandardScaling`
    3. 군집 모델 학습: `KMeans`를 활용하여 3개의 클러스터(`n_cluster=3`)로 분류 → 학습 진행
    4. 시각화

![수행결과 이미지](image/지역별기후클러스터링결과.png)
![수행결과 이미지](image/지역별기후클러스터링(기온범위vs습도대비강수량).png)



---
# 전기 사용량 예측
* **학습 과정**
    * 사용할 변수 선택 : 평균 기온, 최고 기온, 습도
    * 결측치 처리 : feature에 해당하는 컬럼에 결측치 → `.mean`을 통해 각 열의 평균으로 채움
    * 학습 / 테스트 데이터 분할
    * 모델 리스트 정의 : `LinearRegression`, `RandomForest`, `XGBoost` 활용

* **최종 예측 모델 학습 및 평가**
    * 사용할 feature과 target 지정:
      * 수치형 특성 : 평균 기온, 최고 기온, 습도, 월, 연도 / target : 전력 사용량(kWh)
    * 지역 변수 One-Hot Encoding:
      * 범주형 변수 `지역`을 0 or 1로 나누는 One-Hot Encoding 적용 → 새로운 컬럼 생성
    * 사용할 최종 feature 정리:
      * 최종 feature : 수치형 특성 + One-Hot 인코딩 한 지역 컬럼들
    * X, y 데이터셋 생성:
      * X 데이터 : 최종 feature / y 데이터 : target(전력 사용량)
    * PolynomialFeatures를 통한 다항 특성 생성:
      * 수치형 특성들 → 2차항(polynomial_degree=2)으로 확장
      * 다항 확장된 수치형 특성 + 지역 컬럼들 => X_final 데이터로 최종 활용
    * 모델 학습 및 성능 평가
      * 학습/테스트 데이터 분할(학습:테스트 = 8:2)
      * 스케일링 : StandardScaler를 통한 정규화 진행
      * 최종 모델 : Linear Regression(선형 회귀)
      * 성능 평가 : R²(R2 score) → 1에 가까울수록 성능이 좋음.
        | 모델명           | R2   |
        |-----------------|-------|
        |Linear Regression| 0.97057| 

![수행결과 이미지](image/실제vs예측사용량(선형회귀).png)

    

---
# 🪄 성능 향상을 위한 과정
    * 평가 지표 : MAE(Mean Absolute Error), RMSE(Root Mean Squared Error), R²(R2 score)
    * 변수 중요도 시각화 과정
      | 모델명            | MAE            | RMSE           | R2         |
      |------------------|----------------|----------------|------------|
      |Linear Regression| 2.001161e+08 | 3.718493e+08 | -0.011490 |
      |Random Forest    | 2.390083e+08 | 4.274007e+08 | -0.336282 |
      |XGBoost         | 2.548086e+08 | 4.634841e+08 | -0.571439 |


---
# 한 줄 회고
* 이가은 :
* 이민영 :
* 조해리 : 지역별 날씨 데이터를 클러스터링했을 때, 초기 실루엣계수가 0.2로 나와 꽤 충격을 받았다. 이후 파생변수를 추가하고, 차원축소나 모델 변경 등 여러 방법을 시도했지만 최대 0.4까지밖에 끌어올리지 못했다. 비록 결과적으로 발표에 포함되지는 않았지만, 시각화를 통해 계수가 오를수록 군집 구조가 달라지는 모습을 보며 성능 향상의 중요성과 다양한 시도의 필요성을 다시 한 번 느낄 수 있었다.
* 주수빈 : 




