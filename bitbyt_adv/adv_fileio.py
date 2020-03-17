# 파일 IO 연습
"""
- open : 파일을 연다
    모드 r(읽기: 디폴트), w(쓰기), a(추가)
    타입 t(텍스트: 디폴트), b(바이너리)
"""

def write01():
    # 파일을 열기 위해 open
    # w 모드는 이미 파일이 있어도 새로 파일을 작성
    f = open("./sample/test.txt", "w", encoding="utf-8")
    # t가 기본 값이라 생략
    write_size = f.write("I will answer injustice with justice")
    print("{} 만큼 저장:".format(write_size))
    f.close()  # 파일 사용 후 반드시 닫아주기


def write02():
    # append 모드 : 이미 파일이 있으면 내용은 그대로 두고 뒤에 새로 추가
    f = open("./sample/test.txt", "a", encoding="utf-8")
    f.write("Append 모드로 저장하였습니다.")
    f.close()


def copy_binary():
    # 이진 데이터 파일을 다룰 때는 파일 형식을 b로 설정
    f_src = open("./sample/rose-flower.jpeg", "rb")
    # r이 기본값 -> 생략가능
    data = f_src.read()
    f_src.close()

    f_target = open("./sample/rose-flower-copy.jpeg", "wb")
    f_target.write(data)
    f_target.close()


def read01():
    # 파일 읽기 : 전체 데이터 읽기 = read()
    f = open("./sample/sangbuk.csv", "rt", encoding="utf-8")
    text = f.read()
    print(text)
    f.close()


def read02():
    # 파일 읽기 : 줄 단위(\n)로 읽기 = readline()
    f = open("./sample/sangbuk.csv", "rt", encoding="utf-8")
    # print(f.readline())  # 첫줄만 읽어옴
    while True:
        line = f.readline().replace("\n", "")  # 읽어올 데이터가 없으면 "" -> False
        # 이미 파일 안에 개행문자가 있으므로 두줄을 띄우지 않도록 개행 문자를 치환
        if not line: # 비어있으면
            break
        print(line)
    f.close()


def read03():
    # 한번에 읽어와서 줄 단위로 리스트 생성 : readlines
    f = open("./sample/sangbuk.csv", "rt", encoding="utf-8")
    lines = f.readlines()
    print("lines:", type(lines))

    # List 순회
    for index, line in enumerate(lines):
        print("{}번째 line: {}".format(index, line))


def safe_open():
    # 파일 등 시스템 자원을 열게되면 반드시 닫아야 하는데
    # with ~ as 사용시 해당 블록 종료 후 자동으로 close 실행
    with open("./sample/test.txt", "rt", encoding="utf-8") as f:
        print(f.read())
        # close 하지 않아도 됨



# Pickle의 사용
# Python 객체의 직렬화 - 역직렬화를 위한 모듈
# 프로토콜 버전이 있으며 필요할 경우 특정 버전을 이용해 저장 가능
# 파일 저장 기능은 없고 직렬화-역직렬화만 제공
# pickle 모듈을 import
import pickle

def pickle_dump():
    # 직렬화 : dump
    # 사전 객체를 생성 -> 직렬화
    with open("./sample/players.bin", "wb") as f:  # 반드시 binary 모드 설정
        data = {"baseball": 9}
        pickle.dump(data, f)
        # 필요할 경우 세번째 인자로 Pickle Protocol 버전 명시 (맞지 않을 경우 오류 발생)


def pickle_load():
    # 역직렬화 : load
    # dump시 protocol 버전을 명시했어도 load시에는 명시할 필요 없음
    print("현재의 Pickle Protocol:", pickle.HIGHEST_PROTOCOL)
    # players.bin 에서 pickle 객체 역직렬화
    with open("./sample/players.bin", "rb") as f:
        data = pickle.load(f)
        print(data, type(data))


def pickle_dump_multi():
    # 복수 객체의 직렬화
    with open("./sample/players.bin", "wb") as f:
        pickle.dump({"baseball": 9}, f)
        pickle.dump({"football": 11}, f, 1)  # 하위 호환을 위한 버전 변경
        pickle.dump({"basketball": 5}, f, pickle.HIGHEST_PROTOCOL)


def pickle_load_multi():
    # 복수 객체의 역직렬화
    with open("./sample/players.bin", "rb") as f:
        #print(pickle.load(f))
        #print(pickle.load(f))
        #print(pickle.load(f))
        #print(pickle.load(f))  # EOFError
        while True:
            try:
                print(pickle.load(f))
            except EOFError:
                print("더이상 역직렬화 할 객체 없음")
                break


def example():
    # sangbuk.csv -> 불러와서 dict의 list 생성
    # players로 지정
    players = []

    with open("./sample/sangbuk.csv", "rt", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            #print("member:", line)
            lst = line.replace("\n", "").replace(" ", "").split(",")
            #print("lst:", lst)
            player = {
                "name: ": lst[0],
                "number: ": lst[1],
                "height: ": lst[2],
                "position: ": lst[3],
            }
            players.append(player)  # 리스트에 적재
        print("선수 명단:", players)

        # pickle로 객체 저장
        with open("./sample/sangbuk.pickle", "wb") as f:
            pickle.dump(players, f)

        del players

        # sangbuk.pickle로부터 역직렬화 players 적재
        with open("./sample/sangbuk.pickle", "rb") as f:
            players = pickle.load(f)

        print("복원된 선수 목록:", players)




if __name__ == "__main__":
    #write01()
    #write02()
    #copy_binary()
    #read01()
    #read02()
    #read03()
    #safe_open()
    #pickle_dump()
    #pickle_load()
    #pickle_dump_multi()
    #pickle_load_multi()
    example()