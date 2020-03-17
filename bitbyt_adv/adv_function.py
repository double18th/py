# 함수의 스코핑 룰
# Local -> Enclosed -> Global -> BuiltIn
x = 1  # Global 영역 (x : 글로벌 함수)

def scope_func(a):
    print("scope_func:", locals())
    # a -> 외부로부터 넘어온 객체가 local 심볼에 할당된 것
    # x -> 로컬이 아님
    print("x is in global?", "x" in globals())
    return a + x
# scope_func(10)


def scope_func2(a):
    x = 2  # global x와 다른 객체 (local)
    print("x is in global?", "x" in globals())  # True
    print("x is in local?", "x" in locals())    # True
    print("scope_func2:", locals())
    return a + x
# print(scope_func2(10))


def scope_func3(a):
    # 글로벌 객체를 함수 내부에서 사용하고자 할 경우 global 키워드 사용
    global x  # 지금부터 사용할 변수 x는 local 객체의 생성이 아닌 global 객체의 사용이라는 선언
    # 가능하면 글로벌 객체를 내부에서 변경하지 않을 것을 권장
    # 글로벌 시점의 변경 시점을 확인하기 어렵기 때문
    x = 3
    return a + x

# print(scope_func3(10))
# print("x:", x)


# 함수의 선언 (주로 가변인자와 키워드 인자 중심으로 정리)
# 프로그래밍에서의 함수는 기능의 집합
# 입력값이 없거나, 출력값이 없는 경우 존재
# 함수를 종료할 때 return 사용
# return 뒤에 반환값을 명시하면 결과를 받을 수 있다
# 값을 return 하지 않았거나 종료시까지 아무 return 값이 없을 경우 None (Java의 null과 유사) 출력
def times(a, b):
    return a * b

# 함수 자체도 객체로 판단
# 다른 식별자에 할당 / 다른 함수의 인수로 전달 가능
fun = times  # times 함수가 fun이라는 식별자를 갖게 됨
print("fun:", type(fun))
# 객체가 호출 가능한 객체(함수)인지 판별하기 위해 callable 함수(bool) 사용
print("is fun callable?", callable(fun))

# 객체가 함수인지 판별한 후 호출하기
if callable(fun):
    print(fun(10, 20))

# 인수의 기본값
def incr(a, step=1):  # 두번째 인자값은 기본값 1을 가짐
    return a + step

print(incr(10))     # 두번째 인자 step의 기본값인 1로 세팅 = incr(10, 1)
print(incr(10, 2))  # 기본값을 무시하고 새로운 값 할당 가능

# python은 인수의 이름을 명시해 인자 전달 가능. 순서는 중요하지 않음
print(incr(step=3, a=10))  # incr(10, 3)과 동일


# 가변 인수
# 정해지지 않은 개수의 인자를 받을 때 해당 변수의 앞에 * 명시
# -> 순차 자료형으로 변환되어 입력

# 연습 : 여러개의 인자를 넘겨받아 해당 인자가 int, float이면 합산
#        아닐 경우 합산에서 제외. 총합을 return
def get_total(*args):
    total = 0
    #print(args, type(args))
    for x in args:
        # 합산 가능한 타입인지 체크
        if isinstance(x, (int, float)):
            total += x
    return total

print(get_total(1, 2, 3, 4, 5))
print(get_total(1, 2, 3, 4, 5, "Python", (8, 1, 8)))


# 고정인자, 가변인자, 키워드인자
# 순서가 중요. 고정-가변-키워드 순
def func_args(a, b, *args, **kwd):
    # a, b : 고정인자. 반드시 넘겨줘야 함
    # 그 뒤 인자의 목록은 arg로 넘어올 것(tuple)
    # 그 뒤 인자는 키워드(dict)
    print("고정인자:", a, b)
    print("가변인자:", args)
    print("키워드 인자:", kwd)

    if "option1" in kwd:
        print("option 1이 {}로 설정되었습니다".format(kwd["option1"]))
    else:
        print("option1이 설정되지 않았습니다")

func_args(1, 2, 3, 4, 5, 6, option1="옵션1", option2="옵션2")


# 함수도 객체이므로 다른 함수의 인자로 넘기는 것 가능
# Callback 패턴 구현
def calc(a, b, func):
    # 계산을 위한 수 2개, 계산식 함수 func 전달
    # 넘겨받은 func가 호출 가능 객체인지 먼저 확인
    if callable(func):  # func = 함수?
        return func(a,b)  # 계산함수는 외부로부터 주입

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

print(calc(10, 20, plus))
print(calc(10, 20, minus))


# Lambda 함수 : 익명 함수 (일회성 함수)
print("Lambda 사용:", calc(10, 20, lambda a, b: a * b))  # 즉석에서 곱셈 함수 전달

# Lambda 함수를 이용한 sort(sorted) 키함수 정의
words = "Daenrys Stormborn, House of Targaryen".upper().replace(",", "").split()
print("WORDS:", words)
# SORT 할 때 정렬기준 key 함수를 lambda로 전달
# 단의 길이와 역순 정렬 함수를 lambda 전달
sorted_words = sorted(words, key=lambda word:len(word), reverse=True)
print("Sorted Words:", sorted_words)

# 1부터 20까지 수열을 4로 나누었을 때 나머지 순으로 정렬
nums = range(1, 21)
print("nums:", list(nums))  # list로 변경하지 않으면 범위값만 출력
print("SORTED num % 4 ASC:", sorted(nums, key=lambda n: n % 4))










