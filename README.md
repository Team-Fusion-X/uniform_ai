# Uniform_AI (강민지)

### 주요기능
- 모델과 사용자 데이터 비교 후 합격확률 출력

### 라이브러리 설치
<pre>
pip install -r requirements.txt
</pre>

---

### 서버 test

- 프로그램 실행
<pre>
python app.py
</pre>

- Postman 추천

  [POST요청]   http://127.0.0.1:7070/predict  |  raw->json 선택
- input
<pre>
{
  "data_list": ["DGIST", "융복합대학(기초학부)", "종합", 3, 2, 2, 270, 1]  
}
</pre>

- output
<pre>
{
  "합격 확률": "16%"
}
</pre>

---

### 진행 사항

1. Python Selenium을 사용해 데이터 스크래핑 후 2019_pass_or_fail.json에 저장[python_selenium.py]

2. 결측치 처리
  - 최저 지원 유무, 1차 결과, 전형명 같은 경우 명시되어 있지 않은 값이 많아서 요소 자체를 제거

  - 등급으로 예상해서 백분위를 계산하려 했으나 영어가 절대평가로 빠져서 백분위를 예측할 수 없다고 판단 → 결측치가 있는 부분 제거
 
3. 데이터 학습 후 모델 생성[tokenizer_test.ipynb]
4. flask를 이용해 사용자가 입력했을 때 생성한 모델을 바탕으로 예측할 수 있는 로직 설계[app.py]
5. 서버 연결 -> http://127.0.0.1:7070/predict, 위에 로컬 서버 test 부분 참고

---
### 그 외
- 학교, 학과만 묶은 json파일 생성[department_seperate.py, universities_department.json]
<pre>
    {
        "university": "한국기술교육대",
        "department": "디자인건축공학부(건축공학전공)"
    }
</pre>