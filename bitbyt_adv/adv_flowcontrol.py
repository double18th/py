# 모듈명 출력 __name__
print("모듈의 이름:", __name__)
# __name__은 최상위 모듈로, 실행될 때는 __main__
# import 되었을 때는 파일명 그 자체

# 흐름 제어(조건문, 반복문)
def if_statement():
    """
    조건문
    """

    # 키보드로부터 금액을 입력 받고
    # 10,000원 이상 -> by taxi
    # 2,000원 이상 -> by bus
    # 그렇지 않을 경우 -> on foot
    print("===== if elif else")
    # 키보드에서 금액 입력
    money = input("가지고 있는 돈은?")
    money = int(money)  # int로 변환

    message = ""
    if money >= 10000:
        message = "by taxi"
    elif money >= 2000:
        message = "by bus"
    else:
        message = "on foot"

    print("가지고 있는 돈 {}, 이동 방법 {}".format(money, message))


def if_expr():
    """
    조건 표현식
    """
    print("===== if expression")
    money = int(input("가지고 있는 돈은?"))

    message = "by taxi" if money >= 10000 \
                        else "by bus" if money >= 2000 \
                                      else "on foot"
    # ; 이 없는 파이썬은 개행이 일어날 때 코드가 끝났다고 가정하므로 사용

    print("가지고 있는 돈 {}, 이동 방법 {}".format(money, message))


def for_ex():
    """
    for 반복문
    """
    # 인덱스 반복 구문은 없고 순차자료형의 각 요소를 순회하는 Loop
    a = ["개", "고양이", "소", "말"]
    for animal in a:
        print("item:", animal)
    else:
        print("루프가 종료되지 않고 정상 종료되었을 때")

    # 상황 2 : 값과 함께 인덱스도 필요한 경우
    # enumerate 함수 -> (인덱스, 요소값) 튜플
    for index, animal in enumerate(a):
        #print(animal[0], animal[1])
        print("{}번째 동물 {}".format(index, animal))


    # 상황 3 : dict의 순회 -> key 목록을 loop
    dct = {"name":"장슬기", "age":26, "job":"축구선수"}
    for key in dct :
        # 사전의 키가 할당
        print("KEY: {} -> VALUE: {}".format(key, dct[key]))


    # 상황 4 : dict 순회, key - value가 함께 필요한 경우
    for key, value in dct.items(): # (key, value) 쌍 튜플
        print("KEY: {} -> VALUE: {}".format(key, value))


    # 상황 5 : 범위의 Loop -> range(시작, 끝경계, 간격)
    r = range(1, 100)
    # 1 ~ 100까지의 수 중 짝수의 합
    total = 0
    for num in r:
        if num % 2 == 0:
            total += num

    print("1~100 짝수의 합:", total)

    # 연습문제 1. 구구단 출력
    # 연습문제 2. 역역삼각형 그리기
    """
    ***
    **
    *
    """
    # while로도 해보기

    # continue : 아래에 남아있는 문장은 더이상 실행하지 않고 다음 Loop로 이동
    # break : Loop를 더이상 진행하지 않고 밖으로 탈출


def while_ex():
    # 특정 조건이 만족되는 동안 루프를 실행
    # 조건을 True로 부여하면 무한 루프 생성
    # 1부터 100까지 숫자 중 짝수만 합산
    i = 1
    total = 0
    while i <= 100:
        if i % 2 == 0:
            total += i
        i += 1
    else:
        print("루프가 정상 종료되면 실행")
    print(total)


def list_comp():
    """
    List Comprehension
    """
    # 기존 순차자료형을 기반으로 조건에 맞는 데이터를 추출
    # 연산식을 수행하여 새로운 리스트를 생성

    # Syntax: [표현식 for 항목 in 순회가능 객체 if 조건]
    # 조건문은 필수는 아님

    # 기존 방식
    data = range(1, 11)
    # data 객체를 제곱해 새 리스트 생성
    results = []
    for num in data:
        results.append(num * num)

    print("RESULT:", results)

    # 리스트 내포 방식
    results = [num **2 for num in data]
    print("RESULT(내포):", results)

    # 내포시 if 표현식을 연결하면 조건에 맞는 데이터를 추출해 연산에 포함 가능
    words = "I will take what is mine with fire and blood".split() # list
    print("WORDS:", words)
    # words(str list)에서 길이가 3 이상인 요소만 추출하여 새 리스트 생성
    filtered = [word.upper() for word in words if len(word) >= 3]
    print("Filtered Words:", filtered)


    # TODO: 연습문제
    # 1~100까지의 수 중에서 짝수의 리스트를 새로 만들기
    #data2 = range (1, 101)
    #evens = [num for num in data2 if num % 2 ==0]
    #print("even numbers:", evens)


def set_comp():
    """
    Set Comprehension
    """
    # Syntax : {표현식 for 객체 in 순회가능 객체}

    # 예1 : words 내에서 길이가 2 이하인 새로운 셋 생성
    words = "I will take what is mine with fire and blood".split()
    filtered = {word.upper() for word in words if len(word) <= 2}
    print("filtered set:", filtered)

    # 예2 : 문자열 리스트에서 문자열의 길이를 set으로 저장
    filtered = {len(word) for word in words}
    print("filtered set(length):", filtered)


def dict_comp():
    """
    사전의 내포
    """
    # Syntax: {키표현식:값표현식 for 객체 in 순회가능객체}
    words = "I will take what is mine with fire and blood".upper().split()
    print("words:", words)
    # 키:개별 단어 값:해당 단어의 길이
    dct = {word:len(word) for word in words}
    print("dict comp:", dct)



if __name__ == "__main__":
    #if_statement()
    #if_expr()
    #for_ex()
    #while_ex()
    #list_comp()
    #set_comp()
    dict_comp()



