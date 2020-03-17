# datetime은 날짜를 위한 date 객체, 시간을 위한 time 객체를 합친 것
# datetime 모듈을 import 후 사용
import datetime  # 내장 객체

def get_datetime():
    # 시간의 획득
    # 현재 시간 datetime의 now() 메소드
    dt = datetime.datetime.now()  # 모듈datetime.클래스datetime.메소드now()
    print("now:", dt)

    # 특정 날짜와 시간을 구할 때는 생성자 활용
    # 년, 월, 일은 지정 필수
    dt = datetime.datetime(1988, 8, 18)
    print("dt:", dt)
    # 만약 실존하지 않는 날짜라면 ValueError 발생
    # dt = datetime.datetime(1984, 8, 48)

    # 주요 속성
    # year, month, day, hour, minute, second, microsecond, weekday
    print("dt의 연월일:", dt.year, dt.month, dt.day)

    # 요일의 확인 weekday() 메소드
    # 월: 0 ~ 일:6
    print("1988-08-18의 요일:", dt.weekday())

    # datetime에서 날짜만 확인 date() -> date 객체 반환
    # datetime에서 시간만 확인 time() -> time 객체 반환
    nowdate = datetime.datetime.now().date()
    nowtime = datetime.datetime.now().time()

    print("NOWDATE:", nowdate, type(nowdate))
    print("NOWTIME:", nowtime, type(nowtime))
    # date 객체는 datetime이 가진 year, month, day 등 날짜 관련 속성을 그대로 사용
    # time 객체는 datetime이 가진 시간 관련 속성과 메소드들을 그대로 사용


def timedelta_ex():
    # timedelta : 두 datetime 간 차이 값
    current = datetime.datetime.now()
    past = datetime.datetime(2006, 8, 19)  # 과거 날짜 시간
    # 대소 비교 가능 : 미래 > 과거
    print(current > past)  # current가 past보다 미래인가?
    # 두 dattime은 차이값을 구할 수 있다 : timedelta
    diff = current - past
    print(diff, type(diff))

    # timedelta의 total_seconds -> 모든 속성을 합산 초단위로 반환
    print(diff.days, diff.seconds, diff.microseconds, diff.total_seconds())

    if current > past:
        print("부질없다 ", (current - past).days, "일의 시간")

    # datetime과 timedelta의 합산 미래의 어떤 datetime
    # current로부터 365일이 지난 시점의 datetime
    print("current:", current)
    future = current + datetime.timedelta(days=365, seconds=0, microseconds=0)
    print("future:", future)


def format_date():
    """
    날짜의 포매팅 -> 문자열로 반환 : strftime
    """
    # 현재 datetime을 년-월-일 시:분:초 형식으로 바꿔보기
    current = datetime.datetime.now()
    # 문자열로 포매팅
    print(current.strftime("%Y-%m-%d %H:%M:%S"))

    # 포매팅 -> 0000년 00월 00일
    # locale Error (한글 윈도우: MS949)
    import locale
    locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")

    print(current.strftime("%Y년 %m월 %d일"))
    # 문자열로 된 날짜 정보 -> datetime : strptime
    # strptime(문자열, 해독을 위한 형식 문자열)
    s = "2019/11/20 16:00"
    dt = datetime.datetime.strptime(s, "%Y/%m/%d %H:%M")
    print("해독된 datetime:", dt)



if __name__ == "__main__":
    #get_datetime()
    #timedelta_ex()
    format_date()
