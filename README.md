# AI 기반 대학 입시 도움 플랫폼 Uniform_AI (강민지)

### 주요기능

![image](https://github.com/user-attachments/assets/8b7c633c-5d77-48cb-8fbd-0fd776ade8b9)


- 대학교 합불 데이터 스크래핑 후 모델 학습
- 사용자의 성적 데이터를 받아 합격 확률 반환

---
### 진행 사항

1️⃣ Python Selenium을 사용해 데이터 스크래핑 후 2019_pass_or_fail.json에 저장 -> [python_selenium.py](https://github.com/Team-Fusion-X/uniform_ai/blob/main/python_selenium.py)

2️⃣ 결측치 처리

- 최저 지원 유무, 1차 결과, 전형명 같은 경우 명시되어 있지 않은 값이 많아서 요소 자체를 제거
- 등급으로 예상해서 백분위를 계산하려 했으나 영어가 절대평가로 빠져서 백분위를 예측할 수 없다고 판단 → 결측치가 있는 부분 제거

3️⃣ 데이터 학습 후 모델 생성 -> [tokenizer_test.ipynb](https://github.com/Team-Fusion-X/uniform_ai/blob/main/tokenizer_test.ipynb)

4️⃣ flask를 이용해 사용자가 입력했을 때 생성한 모델을 바탕으로 예측할 수 있는 로직 설계 -> [app.py](https://github.com/Team-Fusion-X/uniform_ai/blob/main/app.py)

5️⃣ 서버 연결 -> http://127.0.0.1:7070/predict, 아래 서버 test 참고

---

### 그 외

- 학교, 학과만 묶은 json파일 생성
- json파일 생성 -> [department_seperate.py](https://github.com/Team-Fusion-X/uniform_ai/blob/main/dpartment_seperate.py)
- json파일 -> [universities_department.json](https://github.com/Team-Fusion-X/uniform_ai/blob/main/json_data/universities_departments.json)
<pre>
{
"university": "한국기술교육대",
"department": "디자인건축공학부(건축공학전공)"
}
</pre>

---

### 패키지 설치

```
pip install -r requirements.txt
```

---

### 실행

```
python app.py
```

### 서버 테스트

- Postman 추천
    
    [POST요청]  raw->json 선택 후 http://127.0.0.1:7070/predict로 요청 
    
- input

```json
{
"data_list": ["DGIST", "융복합대학(기초학부)", "종합", 3, 2, 2, 270, 1]
}
```

- output

```json
{
"합격 확률": "16%"
}
```

---

### 기술스택

- Python(Numpy, Pandas)
- Tensorflow/Keras
- Flask
- Selenium

---

### 라이센스

- 대학 입시 정보 페이지 → 서울특별시 교육청의 쎈(SEN)진학 나침판

[진로진학입시사이트 - 수시 합·불 사례](https://ipsi.jinhak.or.kr/subList/20000000292)
