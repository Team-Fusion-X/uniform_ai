# Uniform_AI 작성자 강민지

### 주요기능
- 모델과 사용자 데이터 비교 후 합격확률 출력

### 라이브러리 설치
<pre>
pip install -r requirements.txt
</pre>

---

### 로컬 서버 test
[POST요청]   http://127.0.0.1:7070/predict   raw->json 선택
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
