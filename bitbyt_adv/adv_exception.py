# 예외 처리
"""
try:
    코드
except 익셉션 타입 as 익셉션 할당 변수:
    처리
else:
    정상 수행 되었을 때의 처리
finally:
    예외 여부 관계 없이 항상 마지막에 실행
    주로 자원 정리 작업에 활용
"""

def handling_exception():
    """
    예외 처리 연습
    """
    # 인덱스 에러 IndexError
    # 캐스팅 에러 ValueError
    # 사전 키 접근 에러 KeyError
    # 정수를 0으로 나눴을 경우 ZeroDivisionError

    lst = []

    try:
        #lst[3] = 1  # IndexError
        4 / 0  # ZeroDivisionError
        #int("String")  # ValueError
    except ValueError as e:
        print("정수로 변환할 수 없습니다:", e)
    except ZeroDivisionError as e:
        print("정수를 0으로 나눌 수 없습니다:", e)
    except IndexError as e:
        print("인덱스 범위를 벗어났습니다:", e)
    except Exception as e:
        print("Exception::", e)
    finally:
        print("예외 여부 관계 없이 항상 마지막에 실행")



def raise_exception():
    def beware_dog(animal):
        if animal.lower() == "dog":
            # 강제 익셉션 발생
            raise RuntimeError("개는 출입을 제한합니다")
        else:
            print("어서오세요")
    try:
        beware_dog("cow")
        beware_dog("cat")
        beware_dog("dog")
    except Exception as e:
        print(e, type(e))



if __name__ == "__main__":
    #handling_exception()
    raise_exception()


