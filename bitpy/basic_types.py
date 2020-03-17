# 기초 자료형
def bool_ex():
    print("===== bool 자료형")
    # 참(True), 거짓(False)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판단

    # bool() 논리값 판정 가능
    # 값이 비어있을 경우 False 판정
    # 세팅되어있을 경우 True 판정
    print(bool(0), bool(10))
    print(bool(""), bool("python"))
    print(bool([]), bool([1, 2, 3])) # 순차 자료형의 판정


def int_ex():
    print("===== 정수형 자료")
    # 만드는 방법 : 리터럴, int()
    a = 23
    b = int(23)

    print(a, "is", type(a))
    print(isinstance(a, int))  # a가 int의 객체인지 확인

    # 10진, 2진, 9진, 16진수로 입력
    b = 0b1101   # 2진수는 0b로 시작
    o = 0o23     # 8진수는 0o로 시작
    x = 0x23     # 16진수는 0x로 시작
    print(b, o, x)

    # python 3.x에서는 long, int 구분하지 않고 int 처리
    # long형의 저장 한계점인 64비트(8바이트) 초과한 데이터도 처리
    i = 2 **2048
    print("bit int:", i)
    # 현재 i가 가진 비트수 확인
    print("i의 비트수: ", i.bit_length())

    # 진법 변환 함수 : bin, oct, hex -> 문자열로 반환
    y = 2019
    print("2019->2진수:", bin(y))
    print("2019->8진수:", oct(y))
    print("2019->16진수:", hex(y))


def float_ex():
    print("===== 실수형 연습")
    # float, double 구분하지 않고 float 처리
    f1 = 3.14159
    f2 = float(3.14159)

    print(f1, "is", type(f1))
    print("f2 is float?", isinstance(f2, float))

    f3 = 3.0
    print(f3, "is", type(f3))

    # 형태의 체크 is_integer() -> 정수 형태인지 확인
    # type 비교가 아닌 형태의 판별
    print(f2, "정수 형태?", f2.is_integer())
    print(f3, "정수 형태?", f3.is_integer())

    # 지수 표기법
    # 10의 n승, e 혹은 E를 활용한다
    c = 3e3 # 3 * 10 ** 3
    d = -2E-5 # -2 10 ** 5
    print(c, d)
    print(type(c), type(d))

    print(-2E-5 == -0.00002)  # 같은 표현


def math_functions():
    # 기본적인 수치 함수는 별도 모듈 없이 사용 가능
    # 복잡한 수치 함수는 math 모듈 내부에 있음
    print("===== 내장 수치 함수")
    print("절대값: ", abs(-10))
    print("나눈셈의 몫과 나머지: ", divmod(5, 3))
    # 5를 3으로 나눈 몫과 나머지
    print("제곱 함수: ", pow(2,3))  # 2의 3제곱
    # 특정 수치값을 만들 수 있는 int, float, complex 등의 함수

    # 간단한 통계 함수들은 지원
    scores = [80, 90, 70, 60, 100]
    print("최저 점수(최소값): ", min(scores))
    print("최고 점수(최대값): ", max(scores))
    print("합계: ", sum(scores))
    print("평균: ", sum(scores) / len(scores))


def bit_oper():
    print("===== 비트 연산자")
    # 정수형 데이터를 비트 단위로 제어한다
    # bit NOT ~, 1 <-> 0
    print(bin(5), bin(~5))

    # 비트 시프트 << : 비트를 왼쪽으로 이동
    #             >> : 오른쪽으로 이동
    bits = 1
    print(bin(bits << 4))

    # 비트 and, or
    a = 0b10101010
    b = 0b11110000
    print(bin(a))

    # 비트 and (&) -> 둘 다 1비트가 세팅 -> 1
    print("a & b: ", bin(a & b))
    # 비트 or (|) -> 둘 중 한개의 비트만 1이면 -> 1
    print("a or b: ", bin(a | b))


if __name__ == "__main__":
    #bool_ex()
    #int_ex()
    #float_ex()
    #math_functions()
    bit_oper()
