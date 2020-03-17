# 정규표현식
# 단순 문자열 매칭이 아니라 문자열의 패턴으로 검색
import re

# 사용시 : 패턴 컴파일 -> 패턴 객체의 메소드로 검색 수행
p = re.compile(r"P[a-z]+")
# [] 패턴 1글자 + 1글자 이상
# 대문자 P로 시작 소문자(a-z) 1글자 이상 있는 문자열
print(p.match("Life"))  # 현재 패턴이 Life 일치? -> None. P로 시작하고 한글자 이상이므로
print("p match Python?", p.match("Python"))
print("p match Python?", p.match("Pizza"))

source = "Life is too short, you need Python"
# 방법 1. 패턴 컴파일 후 검색 수행
p = re.compile(r"L[a-z]+")
print(p.match("Life"))

# 방법 2. 축약형, 패턴 문자열과 검색 대상 문자열을 함께 제공
print(re.match(r"[A-Z][a-z]+", source))
# 매치된 내용을 추출할 경우 group() 메소드로 뽑을 수 있다
print("Match된 내용:", re.match(r"[A-Z][a-z]+", source).group())


# 축약 문자
# \d (숫자), \w (문자), \s(공백문자)
# \D (숫자가 아닌 것), \W (문자가 아닌 것), \S (공백문자 아닌 것)
# search -> 전체 문자열 대상 패턴 검색
# findall -> 전체 문자열 대상 검색 후 list로 반환
# finditer -> 검색 후 iterator (반복자)를 반환
source = "Paint C JavaScript 123 456 Perl Java Python P123 Ruby"
# p로 시작되는 문자열 패턴만 검색해서 iterator를 반환
iter = re.finditer(r"\bp\w+", source, re.IGNORECASE)
# re.IGNORECASE : 검색 시 대소문자 구분 없음
for x in iter:
    print("검색된 단어:", x.group())


# 자주 사용될 수 있는 패턴들
# 전화번호의 예
tel = re.compile(r"(\d{2,3})-(\d{3,4})-(\d{4})")
m = tel.match("010-1313-1616")
print("result:", m)
# () 묶은 것은 groups() 메소드로 추출 가능
print("groups:", m.groups())
# 매칭된 전체 내용을 추출: group()
print("매칭된 내용:", m.group())

tel = re.compile(r"(?P<area>\d{2,3})-(?P<exchange>\d{3,4})-(?P<number>\d{4})")
# 그룹핑시 (?P<이름>) 형식을 부여하면 매칭 결과에 이름을 부여할 수 있다
# 이름이 부여된 매칭 결과는 groupdict() 메소드를 사전으로 반환 가능
m = tel.match("010-1313-1616")
print(m.groups())  # 그룹핑된 결과
print(m.group())  # 매칭된 전체 결과
print(m.groupdict())  # 부여한 이름을 기반으로 한 dict 객체 반환

# 이메일
pattern = r"\w+[\w\.]*@[\w\.]*\.[a-z]+"
source = "hongjindal@gmail.com"

print(re.match(pattern, source))

# 한글 매칭 (Unicode 기반)
# 한국어 정규식의 예제
source = "Diana Daenerys Rey 장슬기"
p = re.compile(r"[가-힣]+")
print(p.findall(source))
