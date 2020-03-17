# List 연습
"""
List
- 순차 자료형
  - 순서가 있으며, 길이, 포함 여부 확인 가능(in, not in)
  - 인덱싱, 슬라이싱
  - 연결(+), 반복(*)
- 가변 자료형(mutable)
  - 내부 자료 변경 가능
"""

def define_list():
    """리스트의 정의"""
    lst1 = list()  # 빈 리스트
    print(lst1, type(lst1))
    lst2 = []  # 리터럴을 이용한 빈 리시트
    lst3 = [1, 2, "Python"]  # 내부 요소들은 어떤 객체든 상관 없다
    print(lst3, type(lst3))

    # 다른 순차 자료형을 list() 객체 함수로 list로 변경할 수 있다
    lst4 = list("Python Programming")
    print(lst4)


def list_oper():
    """리스트의 연산자"""
    lst = [1, 2, "Python"]
    # 길이 확인 : len
    print(lst, "length:", len(lst))
    # 포함 여부 확인 : in, not in
    print("1이 lst에 있는가?", 1 in lst)

    # 인덱싱 가능
    print("정인덱싱:", lst[0], lst[1], lst[2])
    print("역인덱싱:", lst[-3], lst[-2], lst[-1])

    # 슬라이싱
    print(lst[1:3])  # 항상 경계에 유의
    print(lst[1:])   # 끝 경계 생략되면 끝까지
    print(lst[0:2])
    print(lst[:2])   # 시작 경계 생략되면 처음부터
    print(lst[:])    # 시작-끝이 모두 생략되면 리스트 전체 -> 복제 가능

    copy = lst[:]    # 전체 리스트의 복제
    print("복제:", copy)
    print("copy is lst?", copy is lst)

    # 연결 (+)
    print(copy + ["Java", True, 3.14159])
    # 반복 (*)
    print(copy * 2)
    # 연결과 반복은 새로운 리스트를 생성한다(원본 유지)

    # append vs extend
    # append는 "마지막"에 새 요소를 추가
    print(copy)
    copy.append([3, 4])
    print("APPEND:", copy)
    # 내부에서 4를 찾아내야 한다면
    print(copy[3][1])
    del copy[3]
    # extend는 인자로 부여된 리스트를 뒤에 연결(확장)
    copy.extend([3, 4])
    print("Extend:", copy)

    # insert(i, x) : i 인덱스에 x를 추가
    copy.insert(2, [1, 2, 3])  # 2번 인덱스 위치에 [1, 2, 3]
    print("INSERT:", copy)

    # 포함 여부 확인 : in, not in
    # copy 리스트 내에서 "Python" 요소 있는지 확인
    print("포함 여부:", "Python" in copy)

    # 인덱스 확인
    # copy 리스트 내부에 "Python" 문자열의 인덱스
    print("Index of Python:", copy.index("Python"))
    # 만약 찾고자 하는 요소가 내부에 없으면 에러 (find는 없음)
    # 없는 요소를 검색할 경우 반드시 포함 여부를 먼저 확인
    # copy 리스트에서 "Java" 검색
    if "Java" in lst:
        print("Index of Java:", lst.index("Java"))
    else:
        print("Java 존재하지 않음")

    # 요소의 개수 파악 : count
    # lst 리스트에서 1의 개수
    print("Count of 1:", lst.count(1))

    # 요소의 삭제 : del(인덱스로 삭제), remove(요소 값의 삭제)
    # remove 역시 삭제할 개체가 내부에 없을 경우 에러 발생하므로
    # 리스트 내부에 해당 객체가 있는지 먼저 확인
    if 3 in copy:
        copy.remove(3)
    print("Remove 3 from lst:", copy)

    # Slice를 이용한 삽입, 변경, 치환, 삭제
    # 메소드보다 Slicing 이용을 권장
    lst2 = [1, 12, 123, 1234, 12345]    # len == 5
    print("lst2:", lst2)
    # Slicing을 이용한 삽입
    # 2번 인덱스 위치에 [10, 20] 추가
    lst2[2:2] = [10, 20]
    print("lst2:", lst2)
    # Slicing을 이용한 삭제
    # 범위를 잡고 해당 범위에 빈 리스트[] 할당
    lst2[2:4] = []
    print("lst2:", lst2)
    # Slicing을 이용한 치환
    # 범위를 잡고 해당 범위에 다른 리스트를 할당
    lst2[1:4] = [10, 20]
    print("lst2:", lst2)

    # Slicing을 이용, 가장 마지막에 삽입 (extend와 비슷)
    lst2[len(lst2):] = [30]
    print("lst2:", lst2)


def list_method():
    """리스트의 메소드
    reverse와 sort
    """

    # reverse : 리스트 요소의 순서를 뒤집는다
    lst = [80, 90, 85, 70, 60, 75, 100, 95]
    # 복제본
    copy = lst.copy()
    print("Reverse 이전:", copy)

    copy.reverse()
    print("Reverse 이후:", copy)

    # sort : 정렬
    # - sorted : 문법상 정렬 함수 -> 정렬 시도한 객체 내용을 변경하지 않음
    # - sort : 객체 내부의 정렬 메소드 -> 객체 내부의 내용을 변경
    # 그 이외의 사용방법 동일
    print("Sorted 이전:", copy)
    print("Sorted 수행:", sorted(copy))  # 기본적으로 오름차순
    print("Sorted 수행 이후:", copy)  # 객체 내부 데이터 변경 없음

    # copy 객체 내부의 sort 메소드 수행
    copy.sort()
    print("Sort 이후:", copy)  # 객체 데이터 변경 확인

    # 역순 정렬 : sort, sorted에 reverse=True를 부여하면 역순 정렬
    copy = lst.copy()
    print("역순 정렬 이전:", copy)
    print("역순 정렬:", sorted(copy, reverse=True))

    # copy를 정수형이 아닌 str 기준으로 역순 정렬
    print("lst str 기준 역순 정렬", sorted(copy, key=str, reverse=True))
    # key 인자값에 두 값을 비교하는 함수를 부여
    # 사용자 정의를 기준으로 한 정렬 가능
    lst = [19, 46, 37, 35, 91, 55, 64]
    # 각 요소 값들을 10으로 나눈 나머지를 정렬 기준으로 설정
    # sort를 위한 key 함수 선언
    def key_func(val):
        return val % 10

    lst2 = sorted(lst, key=key_func)
    print("Custom Sort:", lst2)

    # 문자열의 길이를 대상으로 Sort하는 key 함수
    def key_length(val):
        return len(val)

    words = "I will take what is mine with Fire and Blood".split()
    print("WORDS:", words)
    # 단어의 길이의 역순으로 정렬
    print("단어 길이의 역순 정렬:", sorted(words, key=key_length, reverse=True))


def loop():
    """리스트의 순회"""
    words = "I will take what is mine with Fire and Blood".split()
    print("WORDS:", words)

    # 순차형 자료형은 for ... in ... 문으로 차례대로 요소를 반환 가능
    # 별도의 인덱스 변수는 없음
    for word in words :
        print("Word in words:", word)


def stack_ex():
    """
    리스트를 활용한 stack 구현
    append-pop 메소드를 이용해 stack 자료형 구현 가능
    """
    stack = []
    # input
    stack.append(10)
    stack.append(20)
    stack.append(30)

    # output : input 방향과 동일
    print(stack.pop())
    print(stack.pop(-1))
    print(stack.pop())

    # pop 하기 전에 비어있는지 체크
    if len(stack) > 0:
        print(stack.pop())
    else:
        print("스택이 비어있음")
    print("STACK:", stack)


def queue_ex():
    """
    리스트를 응용한 Queue 구현
    append, pop(0)을 이용해 Queue 자료형 구현 가능
    """
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)

    print("QUEUE:", queue)
    # output은 앞에서부터 : 0번 인덱스
    print(queue.pop(0))

    while(len(queue) > 0):
        print("Queue item:", queue.pop(0))




if __name__ == "__main__" :
    #define_list()
    list_oper()
    #list_method()
    #loop()
    #stack_ex()
    #queue_ex()
