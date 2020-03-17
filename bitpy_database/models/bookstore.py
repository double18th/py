# peewee 모델 생성
import peewee
# 데이터베이스 정보 세팅
database = peewee.SqliteDatabase("mypeewee.db")

# 기본이 될 베이스 모델 - > 각 클래스의 기반 클래스로 활용
class BaseModel(peewee.Model):
    # peewee의 Model 클래스를 부모로 사용
    # 데이터베이스 설정을 위한 inner Class가 필요
    class Meta : # 데이터베이스 설정을 위한 각종 설정값을 부여
        database = database

# Category 모델의 생성
class Category(BaseModel):
    # 매핑 정보의 설정
    no = peewee.IntegerField(primary_key=True)  # PK
    name = peewee.CharField(max_length=20)  # Varchar

    # 출력을 위한 __str__ 오버라이드
    def __str__(self):
        return "Category {}: {}".format(self.no, self.name)

class Book(BaseModel):
    no = peewee.IntegerField(primary_key=True)  # PK
    title = peewee.CharField()
    price = peewee.IntegerField()
    pub_date = peewee.DateField()
    # Relation with Category 카테고리와 관계 맺기
    category = peewee.ForeignKeyField(Category, backref="no",  # 참조 필드
                                                null=True,  # null 허용 여부
                                                related_name="books")
                                                # Category 객체 내부에서 books로 연결된 Book 객체를 확인)
    # 출력을 위한 __str__ 오버라이드
    def __str__(self):
        return "BOOK title:{}, category{}, price:{}".format(self.title, self.category, self.price)


# 모델 객체가 있고, 매핑 정보가 있으므로 별도의 DML 쿼리 불필요
def initialize():
    database.connect()  # DB 접속
    database.create_tables([Book, Category])
    # 모델 매핑 정보를 기반으로 테이블 생성
    database.close()

# 테이블 삭제 함수
def drop_tables():
    database.connect()
    database.create_tables([Book, Category])
    database.close()

# insert 함수 : Book 객체
def insert_book(no, title, pub_date, price, category):
    # insert는 create() 메소드로 객체 생성 후
    # save() 메소드로 데이터베이스에 저장
    b = Book.create(no = no,
                    title = title,
                    pub_date = pub_date,
                    price = price,
                    category = category)
    b.save()  # 실제 테이블에 저장
    return b

def insert_category(no, name):
    c = Category.create(no = no, name = name)
    c.save()  # 실제 테이블에 저장
    return c










