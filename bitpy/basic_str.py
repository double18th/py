def define_str():
    """define_str()
    문자열 정의 연습"""
    # 문자열의 정의
    # 한 줄 문자열의 정의
    s1 = "Hello Python" # 겹따옴표, 홑따옴표 모두 가능
    s2 = str('Hello Python')  # 객체 타입으로 생성
    s3 = str(3.14159)  # 다른 타입을 문자열로 캐스팅

    print(s1, s2, s3)
    print(type(s1), type(s2), type(s3))

    # 인스턴스 체크
    print("s1은 str인가?", isinstance(s1, str))

    # 여러 줄 문자열 : """, '''
    s4 = """파이썬의 여러 줄 문자열은 다양한 용도로 사용되기도 한다"""
    print(s4)

    # 여러 줄 문자열의 활용
    """파이썬은 기본적으로는 여러 줄 주석을 허용하지 않으나
    여러 줄 문자열을 여러 줄 주석으로 사용할 수 있다"""

    # 여러 줄 문자열은 함수, 클래스 선언부 아래쪽에 여러 줄 문자열을 입력하면
    # 문서화, 도움말 출력시 이 문자열을 출력

def string_oper():
    """문자열의 연산자"""
    """str
    - 순차 자료형: len, in, not in, 인덱싱, 슬라이싱
      연결(+), 반복(*)
    - 변경 불가 자료형(immutable)     
    """
    s1 = "First String"
    s2 = "Second String"

    # 길이 : 시퀀스 자료형 len
    print("LEN of s1:", len(s1))
    print("LEN of s2:", len(s2))

    # 인덱싱 : 배열처럼 인덱스로 접근 가능. 시작은 0부터
    # 정인덱싱 : 앞에서부터 인덱싱(0~)
    # 역인덱싱 : 뒤에서부터 인덱싱(-1~. 음수)
    # s1의 6,7,8번 인덱스
    print("6, 7, 8 of s1:", s1[6], s1[7], s1[8])
    print("-6, -5, -4 of s1:", s1[-6], s1[-5], s1[-4])

    print("s1[6] == s1[-6]?", s1[6] == s1[-6])

    # str은 변경불가(immutable)이므로 내부 자료 변경 불가
    # s1[0] = 'f' -> Error

    # 슬라이싱 [시작경계:끝경계] - 인덱싱보다 경계로 이해하는 것이 더 편함
    s3 = s2[7:10]
    print(s3)
    s4 = s2[-6:-3]  # 음수 인덱스를 이용한 슬라이싱
    print(s4)

    print(s2[7:10] == s2[-6:-3])

    # 시작 경계 생략 -> 처음부터
    # 끝 경계 생략 -> 끝까지
    print(s2[7:])
    print(s2[7:] == s2[7:len(s2)])
    print(s2[:6]) # 처음 ~6 경계
    print(s2[:6] == s2[0:6])

    # [시작경계:끝경계:간격값]
    print(s2[0:len(s2):2])
    print(s2[0:len(s2):2] == s2[::2])  # 축약형
    # 간격값이 음수일 경우 방향이 반대
    print(s2[::-1])

    # 연결(+) -> 산술 연산이 아님에 유의
    print(s1 + s2)
    # 반복(*) -> 순차형 * int
    print("Python" * 3)

def transfrom_method():
    """변환 관련 메소드들"""
    """
    - lower, upper : 모두 소문자, 모두 대문자
    - swapcase : 대 <-> 소문자 전환
    - capitalize : 첫번째 글자를 대문자로 변경
    - title : 각 단어의 첫 글자를 대문자 / 나머지는 소문자로
    """

    s = "I like Python"
    print("SWAPCASE:", s.swapcase())
    print("CAPITALIZE:", s.capitalize())
    print("TITLE", s.title())


def search_method():
    """검색 메소드 연습"""
    s = "I Like Python, I Like Java Also"
    print("COUNT:", s.count("Like"))
    # 문자열 찾기 : find, index 계열
    print("FIND:", s.find("Like"))  # 처음부터 검색
    print("FIND AGAIN:", s.find("Like", 6))  # 6번 인덱스부터 검색
    print("FIND 없는 문자열:", s.find("JS"))  # -1
    print("RFIND:", s.rfind("Like"))  # 뒤 -> 앞으로

    print("INDEX:", s.index("Like"))  # 정방향 검색
    print("FIND AGAIN:", s.index("Like", 6))  # 검색범위 제한

    # print("INDEX 없는 문자열:", s.index("JS"))
    # index는 없을 경우 명시적으로 Error 발생
    # 미래 내부에 검색값이 있는지 먼저 확인 필수
    if "JS" in s :
        print("Safe Index:", s.index("JS"))
    else:
        print("JS는 없어요!")

    # 역방향 검색 : rfind, rindex
    print("RFIND:", s.rfind("Like"))
    print("RFIND Again:", s.find("Like", 0, 17))  # 거꾸로 들어가는 것이므로 끝 범위를 꼭 정해줘야함
    # rindex도 마찬가지 방법으로 수행
    # 오류 발생 가능 -> 포함 여부를 먼저 판별한 후 수행

    # 특정 문자열로 시작 or 끝나는지 판별
    # startswith, endswith
    url = "http://naver.com"
    surl = "https://naver.com"
    ftp = "ftp://naver.com"

    print("startswith http?", url.startswith("http://"))
    print("startswith https?", surl.startswith("https://"))
    # 문자열이 여러 검색어 중 한개로 시작하는가?
    print(ftp, "startswith http or ftp?",
          ftp.startswith(("http://", "ftp://")))
    # url이 .com으로 끝나는가?
    print(url, "endswith .com?", url.endswith(".com"))
    # startswith, endswith도 시작 범위, 끝범위를 잡을 수 있다
    # ftp 문자열 6부터 11까지의 문자열이 na로 시작하는가?
    print(ftp, "(6, 11) startswith na?", ftp.startswith("na", 6, 11)) # 6~11 범위로 검색 제한


def modify_and_replace():
    """문자열 수정과 치환 관련 메소드"""
    s = "          Daenerys Stormborn   "
    print("STRIP: [", s.strip(), "]", sep="")
    print("LSTRIP: [", s.lstrip(), "]", sep="")
    print("RSTRIP: [", s.rstrip(), "]", sep="")

    s2 = "------House of Targaryen-------------"
    print("STRIP -: [", s2.strip("-"), "]", sep="")

    # 치환 : s문자열을 strip, Stormborn -> Targaryen으로 치환
    print(s.strip().replace("Stormborn", "Targaryen"))

    print("ORIGINAL s:", s)  # 문자는 불변형이므로 원본은 고정


def align_methods():
    """문자열 정렬"""
    # 기본적으로 출력 자리수를 정해두고 내부에 문자열 출력시
    # 출력 방향을 지정(정렬)
    s = "Daenerys Stormborn"
    print("CENTER:[", s.center(60), "]", sep="")  #60자리 확보 중앙 정렬
    print("CENTER:[", s.center(60, "*"), "]", sep="")  #60자리 확보 중앙 정렬, 공백은 *로 대체
    print("LJUST:[", s.ljust(60, "*"), "]", sep="")  #60자리 확보 좌측 정렬, 공백은 *로 대체
    print("RJUST:[", s.rjust(60, "*"), "]", sep="")  #60자리 확보 우측 정렬, 공백은 *로 대체

    # zfill : 빈공간을 0으로 채움
    print("ZFILL:", "1234".zfill(5))  # 총 자리수


def split_and_join():
    """나누기와 합치기"""
    s = "Daenerys and Drogon and Viserion and Rhaegal"
    print("SPLIT:", s.split())  # 공백문자 기준으로 분리
    drgn = s.split(" and ")  # 특정 문자열을 기준으로 분리
    print("가족들:", drgn)
    # ,문자로 list 각 요소를 합치기 : join

    print("JOIN with ,:", ",".join(drgn))

    # split시 분리하고자 하는 요소의 개수 지정
    print(s.split(" and ", 2))  # 구분자를 기준으로 2개만 추출
    print(s.rsplit(" and ", 2))  # 구분자를 기준으로 오른쪽에서 2개 추출


    # 여러 줄 문자열이 있을 때 개행 문자를 기준으로 분리
    # splitlines

    lines = """Java
    Python
    JavaScript
    HTML/CSS"""

    print("SPLIT:", lines.split())
    print("SPLITLINES:", lines.splitlines())  # 개행문자(\n)을 기준으로 분리

    # 개행 문자 유지해야할 경우는 splitlines(True)
    print("SPLITLINES 개행 문자 유지:", lines.splitlines(True))


def check_methods():
    """is 계열 메소드: 형태 판별
    반환값으로 bool(True, False) 반환"""

    print("1234".isdigit())      # "1234"가 숫자 형태?
    print("abcd".isalpha())      # "abcd"가 알파벳 형태?
    print("Python3".isalnum())   # Python3"가 알파벳과 숫자의 조합?
    print("Python 3".isalnum())  # Python3"가 알파벳과 숫자의 조합? -> 공백 포함이므로 False
    print(" \r\n\t".isspace())   # 공백문자 :  스페이스, 개행문자, 탭문자 모두 공백으로 간주
    print("".isspace())          # 값이 없는 것은 공백문자가 아님

    # 알파벳 형태 판별
    print("PYTHON".isupper())  # 모두 대문자인가?
    print("python".islower())  # 모두 소문자인가?
    print("Python Programming".istitle())  # 타이틀(어절 제일 첫글자가 대문자) 형태인가?


def str_format():
    """문자열 포맷 연습"""

    # C-Style의 포맷
    # %s(문자열), %c(문자 1개), %d(정수), %f(실수)
    # %o(8진수), %x(16진수), %% (% Literal)
    # @개의 @ 중에서 @개를 먹었다
    fmt = "%d개의 %s중에서 %d개를 먹었다"
    # 포맷 서식에 데이터 연결 %
    print(fmt % (10, "사과", 3))
    status = "%d마리의 %s중에서 %s만 남았다"
    print(status % (3,"용","드로곤"))
    # 특정 서식 문자들은 옵션이 있을 수 있다. ex.%f
    print("현재 이자율은 %f%%" % 1.24) # %% -> %
    print("현재 이자율은 %.2f%%입니다" % 1.24)  # 소수점 2자리까지

    # named formatting : 각 서식 문자열에 이름 부여 가능
    # 이름 부여 -> 순서는 중요하지 않음
    # 이름이 부여된 서식에 연결할 데이터는 모두 있어야함
    fmt = "%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다"
    print(fmt % {"fruit":"오렌지", "eat":5, "total":13})

    status = "%(dragon)d마리의 %(children)s 중에서 %(remain)s만 남았다"
    print(status % {"dragon":3, "children":"드래곤", "remain":"드로곤"})

    # place holder 방식 : {} -> 연결할 데이터 타입을 가리지 않는다
    fmt = "{}개의 {} 중에서 {}개를 먹었다"
    # .format 메소드를 이용 데이터 바인딩 수행
    print(fmt.format(10, "사과", 3))

    # numbered placeholder 방식 : {번호}
    # named 혹은 numbered 방식은 하나의 데이터를 여러번 바인딩할 경우 유용
    fmt = "{0}개의 {2} 중에서 {1}개를 먹었다"
    print(fmt.format(10, 3, "블루베리"))
    status = "{0}마리의 {2} 중에서 {1}마리가 남았다"
    print(status.format(3, 3, "용"))
    print(status.format(3, 2, "용"))
    print(status.format(3, 1, "용"))
    # named placeholder
    fmt = "{total}개의 {fruit} 중에서 {eat}개를 먹었다"
    # 인자값을 이용한 데이터의 바인딩
    print(fmt.format(total=10, fruit="사과", eat=3))
    # 사전(dict)를 이용한 데이터의 바인딩 .format_map() 메소드로
    dct = {
        "total":10,
        "fruit":"오렌지",
        "eat":5
    }
    print(fmt.format_map(dct))



if __name__ == "__main__":
    #define_str() # 문자열 생성 연습
    #string_oper()
    #transfrom_method()
    #search_method()
    modify_and_replace()
    #align_methods()
    #split_and_join()
    #check_methods()
    str_format()