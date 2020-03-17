# class
"""
- 새로운 이름 공간을 지원하는 단위: 데이터의 설계도
- 새로운 클래스는 새로운 자료형을 정의하는 것
- 인스턴스는 이 자료형의 객체를 생성하는 것
- 클래스와 인스언스는 직접적인 연관관계를 갖는다

- 인스턴스에서 클래스 멤버의 접근은 가능
- 클래스 멤버에서 인스턴스 멤버의 접근은 불가
"""


class MyString(str):  # str은 상속받지 않은 새로운 클래스
    pass;

# 특정 클래스를 상속받지 않은 경우, object 상속
s = MyString()  # 생성자 호출
print(type(s))

# 어떤 클래스를 상속받은 클래스인가?
# __bases__ => 부모의 목록을 튜플로 반환
print("MyString의 부모:", MyString.__base__)

# 특정 부모를 상속받지 않을 경우 () 없어도 된다
class myobj: #object를 상속
    pass

print(myobj.__bases__)

# 파이썬은 여러 부모로부터의 상속을 허용한다
class Complex(str, myobj):
    # str로부터 모든 멤버들, # myobj로부터 모든 멤버들을 물려받음
    pass

print("Complex,; 부모:", Complex.__base__)

# 특정 클래스가 다른 클래스의 자식인지 확인
# issubclass 함수
print("Complex가 str의 자식인가?", issubclass(Complex, str))


# 클래스의 생성
# 인스턴스를 위한 멤버는 항상 self를 붙여준다
class Point:
    # 클래스 멤버 :
    # 클래스 이름 공간 내에 생성, 모든 인스텐스 멤버 공유
    # 클래스 멤버는 인스턴스 생성 없이 사용 가능
    instance_count = 0

    def __init__(self, x=0, y=0):  # 생성자
        # 파이썬에서는 생성개를 여러개를 만들 수 없으므로
        # 범용적으로 사용 가능한 유일한 생성자를 작성
        self.x = x
        self.y = y
        # instance_count 참조하고자 할때는 괜찮으나 변경은 아래 방식으로
        Point.instance_count += 1

    def __del__(self):  # 소멸자
        # 객체가 제거될 때 호출
        Point.instance_count -= 1

    def __str__(self):  # 문자열 출력
        # 비공식 문자열(일반 사용자 대상)
        # str() 호출 혹은 print시 사용됨
        return "Point x={}, y={}".format(self.x, self.y)

    def __repr__(self):  # 문자열 출력 02
        # 공식 문자열 (개발자 대상)
        # repr() 함수로 전달 받을 수 있음
        # 이 문자열로 해당 객체 복원이 가능해야함
        return "Point({}, {})".format(self.x, self.y)

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    # 연산자 오버로딩
    # 새로운 데이터 타입에 필요한 연산자의 행동을 재정의하는 것
    # 산술 연산자 오버로딩 예제
    def __add__(self, other):
        # Point(self) + other
        # other 타입을 점검해 각기 다른 행동을 취하도록
        """
          1) Point + Point
          Point(10, 20) + Point(20, 30) == Point(30, 50)

          2) Point + int
          Point(10, 20) + 10 == Point(20, 30)
        """
        if isinstance(other, Point):
            # 합산된 객체가 Point
            self.x += other.x
            self.y += other.y
        elif isinstance(other, int):
            # return Point(self.x + other, self.y + other)  값이 변경되지않길 원할 경우
            self.x += other
            self.y += other
        else:
            self += other  # 의미 없는 자리 채움

        return self

    # 역이항 연산자: other + Point
    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self)
        elif isinstance(other, int):
            self.x += other
            self.y += other
        else:
            self += other
        return self


def bound_class_method():
    # 생성된 인스턴스를 통해 직접 메소드에 접근하는 방법
    p = Point()
    # bound 방식인 경우, 첫번째 인자 self는 전달 불필요
    p.setX(10)
    p.setY(20)

    print("Point p: {}, {}".format(p.getX(), p.getY()))
    print(p.getX, p.getY)

#bound_class_method()
def unbound_class_method():
    # 클래스를 통해 우회 접근하는 경우
    # 메소드에 부여된 self 인자에 실제 객체의 주소 전달
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)

    print("Point p: {}, {}".format(Point.getX(p), Point.getY(p)))
    print(Point.getX, Point.getY)

#unbound_class_method()

def class_member():
    p1 = Point()
    p2 = Point()

    # 클래스 멤버는 모든 인스턴스에서 접근 가능
    # 생성 없이도 직접 접근 가능
    print("p1의 instance_count의 주소:", id(p1.instance_count))
    print("p2의 instance_count의 주소:", id(p2.instance_count))

    # 클래스 멤버의 변경
    Point.instance_count += 1
    print("p2의 instance_count:", p2.instance_count)

#class_member()

def lifecycle():
    # 생성자와 소멸자 테스트
    p1 = Point()  # 생성자의 기본값이 사용
    print(p1)
    print("instance_count:", Point.instance_count)

    p2 = Point(x=20, y=30)
    print("instance_count:", Point.instance_count)

    del p2
    print("instance_count:", Point.instance_count)

#lifecycle()

def str_repr():
    p = Point(10, 20)
    print(p)  # __str__ 호출
    print("포인트 p=" + str(p))  # __str__ 테스트

    # repr 함수를 사용하면 __repr__ 문자열을 얻을 수 있다
    print("repr of p:", repr(p))

    # eval 함수를 사용해 파이썬 코드 테스트 가능
    # repr로 전달 받은 문자열(개발자용)을 넘겨주면 같은 객체가 복원되어야 함
    p_repr = eval(repr(p))
    print(p_repr, type(p_repr))

#str_repr()


def test_overloading():
    # 연산자 오버로딩
    p = Point(10, 20)
    print("p:", p)
    p2 = Point(30, 40)

    print("산술연산자 테스트:", p + p2)  # Point + Point
    print("Point + int:", p + 20)       # Point + int
    print("int + Point:", 20 + p)
    # 20 + p로 쓰면 에러 발생
    # int 기준으로는 Point와의 합산이 불가능하므로
    # 역이항 연산자를 사용하여 Point 기준으로 합산을 재정의해야함

test_overloading()