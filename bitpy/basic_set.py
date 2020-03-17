# Set 연습
evens = {0, 2, 4, 6, 8}  # 짝수 집합
odds = {1, 3, 4, 7, 9}   # 홀수 집합
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  # 전체 집합
mthree = {0, 3, 6, 9,}  # 3의 배수 집합

def define_set():
    """Set 정의 연습"""
    """
    Set 
    - 순서가 없으며 중복을 허용하지 않음
    - 인덱싱 및 슬라이싱 불가
    - len, 포함 여부(in, not in) 사용 가능
    - 집합을 표현하는 자료형(집합 연산 가능)
    """

    # 리터럴 기호{}
    # {} : set - dict 양쪽에서 공유하므로 Empty Set을 만들 때는 {} 사용 불가
    # 값이 있을 때는 상관없음 (dict는 key-value 값이 와야하므로 구분 가능)
    s = set()  # s = {}
    print("s:", type(s))

    # 길이와 포함 여부는 확인 가능함
    print(numbers, "LENGTH:", len(numbers))
    # 2가 각 집합에 포함되어 있는가?
    print(2 in numbers, 2 in evens,
          2 in odds, 2 in mthree)

    # set 객체 함수를 이용, 다른 순차 자료형을 set으로 캐스팅 가능
    s = "Python Programming"
    print(s, "LENGTH:", len(s))
    chars = set(s.upper())
    print(chars, "LENGTH:", len(chars))
    # 중복 허용하지 않는 특성
    # -> 리스트 등 자료형에서 중복 제거시 유용
    lst = "Python Programming Java Programming R Programming".split()
    print(lst)
    lst = list(set(lst))
    print("중복 제거:", lst)


def set_methods():
    """
    Set의 메소드들
    """
    # 요소의 추가 : add
    numbers.add(10)
    print(numbers)

    print("evens:", evens)
    evens.add(2)  # 중복 추가되지 않음 -> 집합
    print("evens:", evens)

    # 요소 삭제
    # - discard : 요소 삭제 -> 요소가 없어도 오류 발생하지 않음
    # - remove : 요소 삭제 - > 요소가 없으면 오류
    numbers.discard(10)
    print("numbers:", numbers)
    numbers.discard(10)  # 요소가 없어도 오류 없음

    if (10 in numbers):
        numbers.remove(10)  # 요소가 없으면 오류 발생
    else:
        print("삭제할 요소 없음")

    evens.update({10, 12, 14, 16})  # 여러 요소를 한번에 업데이트
    print("evens:", evens)

    evens.clear()  # 셋 비우기
    print("evens:", evens)


def set_oper():
    """
    집합 연산
    """
    # 합집합 : |, union 메소드
    print("짝수와 홀수 합집합:", evens.union(odds))
    print(evens.union(odds) == numbers)
    print(evens | odds == numbers)

    # 모집합, 부분 집합의 판단 issuperset, issubset
    print(numbers.issuperset(evens), numbers.issuperset(odds))
    print(evens.issubset(numbers), odds.issubset(numbers))
    print(evens.issuperset(odds))

    # 교집합 : &, intersection 메소드
    print(evens.intersection(mthree) == {0, 6})  # 짝수--3의 배수의 교집합
    print(odds & mthree == {3, 9})  # 홀수와 3의 배수의 교집합

    # 차집합 : -, difference 메소드
    print(numbers.difference(evens) == odds)  # 전체 수와 짝수의 차집합
    print(numbers - odds == evens)  # 전체 수와 홀수의 차집합


def loop():
    """
    세트의 순회
    """
    print("numbers:", numbers)
    # 순회
    for item in numbers:
        print(item, end="")
    print()


if __name__ == "__main__":
    #define_set()
    #set_methods()
    #set_oper()
    loop()
