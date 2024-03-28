import json

# JSON 파일 불러오기
with open('json_data/2019_pass_or_fail.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

universities = {}

# 주어진 데이터를 활용하여 대학 및 학과 정보를 딕셔너리로 정리
for entry in data:
    university_name = entry["대학명"]
    department = entry["학과명"]
    
    if university_name in universities:
        universities[university_name].append(department)
    else:
        universities[university_name] = [department]

# 중복된 값 제거 후 딕셔너리 값 갱신
for university in universities:
    unique_departments = list(set(universities[university]))
    universities[university] = unique_departments

# JSON 파일로 저장
with open('json_data/universities_departments.json', 'w', encoding='utf-8') as f:
    json.dump(universities, f, ensure_ascii=False, indent=4)