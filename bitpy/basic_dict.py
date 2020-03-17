# dict 예제
def define_dict():
    """
    사전의 정의
    """
    # 기본적인 사전의 생성
    dct = dict()  # 빈 사전
    print(dct, type(dct))
    # Literal 이용한 생성 {}
    dct = {"basketball": 5, "baseball": 9}
    # 키에 접근하고자 할 경우
    print(dct["baseball"])  # baseball 키에 연결된 값을 참조
    # 없는 키에 연결된 값의 참조
    #print(dct["soccer"])  : 오류 발생
    dct["soccer"] = 11  # 새 값을 넣을 경우 새로운 키 생성
    print("dct:", dct)

    # 순서가 없기 때문엔 인덱싱, 슬라이싱이 불가
    # len, 포함 여부 (in, not in) 확인 가능
    # 기본적으로 대상이 Key를 기준으로 함(값이 아님)

    # 길이의 확인 : len
    print(dct, "LENGTH:", len(dct))

    # in, not in 키를 검색할 수 있다
    print("soccer" in dct)  # 키 목록에서 soccer 검색
    print("volleyball" in dct)  # 없는 값을 검색(Key 검색)

    # dict는 복합 자료형 -> 키/값의 목록을 별도로 추출 가능
    print("KEYS of dct:", dct.keys())  # keys 메소드 -> 키 목록
    print("Type of keys:", type(dct.keys()))
    print("Values of dct:", dct.values())  # values 메소드 -> 값 목록

    # 값의 포함 여부를 판단 -> .values() dict_values 추출 후 확인
    # dct의 값 중 9가 포함되어 있는가?
    print("9 in dct.values()?", 9 in dct.values())

    # 사전을 생성하는 다른 방법들
    # 키워드 인자를 이용한 사전 생성
    d1 = dict(key1="value1", key2="value2", key3="value3")
    print("d1:", d1, type(d1))

    # 튜플의 리스트로 사전 생성
    d2 = dict([("key1", 1), ("key2", 2), ("key3", 3)])
    print("d2:", d2, type(d2))

    # 키의 목록과 값이 목록이 이미 있는 경우
    # zip 객체로 묶어서 dict에 전달
    keys = ("one", "two", "three", "four")
    values = (1, 2, 3, 4)
    d3 = dict(zip(keys, values))
    print("d3:", d3, type(d3))

    # 사전의 키는 immutable 자료형이어야 함
    d4 = {}
    d4[True] = "true"
    d4[10] = 10
    d4["eleven"] = 11
    d4[("홍길동", 23)] = "홍길동 23"
    # bool, 수치형, 문자열, 튜플 등 불변 자료형 가능
    #d4[["홍길동", 23]] = "홍길동 23" -> 오류 발생
    print("d4:", d4)


def dict_methods():
    """
    사전의 메소드들
    """
    dct = {"soccer": 11, "baseball": 9, "volleyball": 6}
    print("dct:", dct)
    # key의 목록 추출 : keys 메소드
    keys = dct.keys()
    print("keys of dct:", keys, type(keys))
    # dict_keys는 순차 자료형으로 변환 가능
    keys_list = list(keys)
    print(keys_list)
    # 값의 목록 추출 : values 메소드
    values = dct.values()
    print("Values of dct:", values, type(values))
    # 키-값 쌍의 튜플 목록 추출
    pairs = dct.items()
    print("key-value pair of dct:", pairs)

    dct.clear()  # 비우기
    print("dct:", dct)


def using_dict():
    """
    사전 사용 연습
    """
    phones = {
        "장슬기": "010-1616-0530",
        "전가을": "010-1313-0914",
        "조소현": "010-0707-0707"
    }
    print(phones)

    # 새로운 키의 추가 ['키']
    phones['지소연'] = "010-1010-1010"
    print(phones)

    # 키 직접 접근 vs get 비교
    if "기성용" in phones:
        print(phones['기성용'])  # 키 직접 접근은 키 부재시 오류 발생
    print(phones.get('기성용'))  # get 메소드는 키 부재시 None 리턴
    # 키가 없어도 기본값을 리턴하고자 하는 경우 get메소드 두번째 인자로 기본값 부여
    print(phones.get("기성용", "미등록"))

    # 삭제 : del
    if "지소연" in phones:
        del phones['지소연']
    print(phones)

    # pop 메소드 : 값을 가져오며 해당 객체를 삭제
    print(phones.pop("조소현"))
    print(phones)
    # popitem 메소드 : 키-값 쌍의 튜플을 반환하고 키 삭제
    item = phones.popitem()
    print("Name:", item[0], "Phone:", item[1])
    print(phones)


def loop():
    """
    사전 객체의 순회
    """
    phones = {
        "장슬기": "010-1616-0530",
        "전가을": "010-1313-0914",
        "조소현": "010-0707-0707"
    }
    print(phones)

    # 기본적인 Loop
    for key in phones:  # 루프를 진행하면 keys() 목록이 대상
        print(key, ":", phones[key])

    # 키-값을 함께 Loop
    for key, value in phones.items():  # items 메소드는 키-값 쌍 튜플의 목록
        print(key, ":", value)



if __name__ == "__main__":
    #define_dict()
    dict_methods()
    #using_dict()
    #loop()
