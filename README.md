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
[기사 링크](https://www.hankyung.com/article/202507100041i)
날이 갈수록, 해가 지날수록 우리나라의 평균 기온과 최고 기온, 최저 기온은 상승하며, 점차 그 예측 속도와 범위를 벗어나고 있는 상황이다. 이러한 상황 속에서 때이른 폭염과 길어지는 여름철 날씨는 냉방 가동을 가속화시켜 여름철 전력 수급에 큰 어려움을 겪게 한다. 따라서 지역별 여름철 날씨 데이터와 전국 전력 사용량 데이터를 활용해 전력 사용량 추이를 분석하고, 여름철 전력 사용량을 예측할 수 있는 모델을 만들어 여름철 전력 수급에 있어 도움을 주고자 한다. 


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
| 시각화                 | <img src="https://img.shiel능

---
# 한 줄 회고
* 이가은 :
* 이민영 :
* 조해리 : 지역별 날씨 데이터를 클러스터링했을 때, 초기 실루엣계수가 0.2로 나와 꽤 충격을 받았다. 이후 파생변수를 추가하고, 차원축소나 모델 변경 등 여러 방법을 시도했지만 최대 0.4까지밖에 끌어올리지 못했다. 비록 결과적으로 발표에 포함되지는 않았지만, 시각화를 통해 계수가 오를수록 군집 구조가 달라지는 모습을 보며 성능 향상의 중요성과 다양한 시도의 필요성을 다시 한 번 느낄 수 있었다.
* 주수빈 : 리드미를 본격적으로 맡아 작성한 프로젝트는 처음인데, 리드미 백업이 정말 중요하다는 것을 몸소 느꼈다.. 또한 지역별 날씨 데이터 클러스터링에서 0.2로 나온 실루엣 계수를 높이기 위해 컬럼을 추가해 보았으나 되려 계수값이 떨어지는 이상한 현상을 목격하기도 했다. 이후 PCA를 통한 차원 축소를 진행하자 그나마 0.4 정도로 오르는 것을 보고 실루엣 계수 향상이 참 어렵다고 느끼는 한편, 차원 축소를 통한 분류 정확도 상승을 직접 경험할 수 있었다. 



