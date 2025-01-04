import re

# 소문자로 치환
new_id = new_id.lower()

# 정규식을 이용한 특수문자 제거
new_id = re.sub('[^a-z0-9-_.]', '', new_id)

# 마침표 중복 제거
new_id = re.sub('\.+', '.', new_id)

# 처음과 끝 마침표 제거
def remove_dot(string):
    return string.strip('.')
new_id = remove_dot(new_id)

# 빈 문자열일 경우
new_id = 'a' if len(new_id) == 0 else new_id

# 문자길이 최대 15로 조정
if len(new_id) >= 16:
    new_id = new_id[:15]
    new_id = remove_dot(new_id)

if len(new_id) <= 2:
    while len(new_id) == 3:
        new_id += new_id[-1]

