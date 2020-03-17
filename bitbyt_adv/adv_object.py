# 객체의 이해
# 글로벌 변수
# 모듈 전체에서 공유된느 심볼들
g_a = 1
g_b = "장슬기"

def func():
    # 내부에 로컬 심볼 영역이 생성
    # 객체에 접근할 경우, 로컬 영역 먼저 확인
    # 없을 경우 상위로 이동하여 검색
    l_a = 2
    l_b = "전가을"
    # local 영역 심볼테이블 확인
    print(locals())

class MyClass:
    x = 10
    y = 10

def symbol_table():
    # 전역 변수 심볼테이블을 출력
    print(globals())
    print(type(globals()))
    # dict로 변환
    # 앞 뒤에 __ -> 심볼들은 파이썬 내부에서 사용하는 심볼. 변경하지 말 것

    func()

    # globals() 반환값이 dict
    # 포함 여부 확인
    print("g_a in global?", "g_a" in globals())

    # 내부에 __dict__를 확인하면 해당 객체 내부의 심볼 테이블 확인 가능

    # 사용자 정의 함수 func의 심볼 테이블을 확인
    print(func.__dict__)  # 출력되지 않으므로 추후 확인 예정
    print(MyClass.__dict__)


def object_id():
    # 변수는 심볼명-객체 주소 값을 함께 가지고 관리됨
    # id() 함수로 객체의 주소 확인
    # is 연산자로 두 객체의 동일성 확인 가능
    i1 = 10
    i2 = int(10)
    print("int:", hex(id(i1)), hex(id(i2)))

    print(id(i1) == id(i2))
    # 두 객체의 id() 값이 동일하다면 두 객체는 같은 객체
    print(i1 is i2)  # 두 객체가 동일 객체인지 (같은 주소인지) 확인하는 연산자

    # mutable 객체
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]

    print("lst1 == lst2 ?", lst1 == lst2)
    print("lst1 is lst2 ?", lst1 is lst2)
    # == : 동등성의 비교, is : 동일성의 비교

def object_copy():
    a = [1, 2, 3]
    b = a  # 단순 레퍼런스 복사
    print(a, b)

    b[0] = 4
    print(a, b)  # 단순 레퍼런스 복사는 주소값만 복사됨

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [a, b, 100]

    print(c)

    # 객체 복제를 위한 copy import
    import copy
    # c를 복제해서 새객체 생성 d에 할당
    d = copy.copy(c)
    print(d)

    d[2] = 10
    print(c, d)

    d[1][0] = 10
    print("얕은 복제:", c, d)
    print("얕은 복제: c is d?", c is d)
    print("얕은 복제: c[0] is d[0]?", c[0] is d[0])
    # 얕은 복제 : 새 객체를 만들지만 내부 요소의 주소값들을 그대로 복제
    # 이 문제 해결을 위해서는 깊은 복제(= 재귀적 복제) 필요
    d = copy.deepcopy(c)
    print("깊은 복제:", c,d)

    # c[0] 객체와 d[0] 객체는 같은 객체인가?
    print("c is d?", c is d)
    print("c[0] is d[0]?", c[0] is d[0])



if __name__ == "__main__":
    #symbol_table()
    #object_id()
    object_copy()