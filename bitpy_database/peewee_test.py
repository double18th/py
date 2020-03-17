#pip install peewee
from models.bookstore import Book, Category
import models.bookstore as bs
# bookstore 모듈을 bs 별칭으로 import

# 테이블 생성 테스트 : 모델 매핑 정보를 기반으로
def create_table_test():
    bs.initialize()

# INSERT와 Relation 테스트
from datetime import datetime
def insert_relation_test():
    # 카테고리 생성
    c1 = bs.insert_category(no = 1, name = "Python")
    c2 = bs.insert_category(no = 2, name = "Java")

    # Book INSERT
    bs.insert_book(no = 1, title = "Learning Python", pub_date=datetime(2015, 11, 13),
                   price = 10000, category=c1)  # c1은 Foreign Key 참조
    bs.insert_book(no=2, title="히치하이커 Python", pub_date=datetime(2008, 5, 22),
                   price=18000, category=c1)
    bs.insert_book(no=3, title="Effective Java", pub_date=datetime(2016, 8, 19),
                   price=21000, category=c2)
    bs.insert_book(no=4, title="God of Java", pub_date=datetime(2014, 11, 14),
                   price=15000, category=c2)


# Update
# 별도 메소드 없으며, get 등으로 메모리에 적재 이후 필드 변경, save() 메소드 수행
def update_test():
    # title이 Effective Java인 책을 찾아 가격을 변경
    book = Book.get(Book.title == "Effective Java")
    print(book)  # __str__
    # 업데이트 할 필드 수정
    book.price += book.price * 0.1  # 10% 인상
    print("업데이트 된 Book 객체:", book)  # __str__
    book.save()  # 저장 -> 업데이트

# Delete : .get 메소드 등으로 메모리에 적재한 후
# delete_instance() 메소드로 메모리에서 삭제하면 테이블에서도 삭제
def delete_test():
    book = Book.get(title = "God of Java")
    # 메모리에서 삭제 -> delete
    book.delete_instance()


# select
def select_test():
    books = Book.select()  # 모든 컬럼의 모든 레코드를 추출
    print(books.sql())  # 실제 수행된 SQL 문 확인 가능

    for book in books:
        print(book)


# select 컬럼의 제한 : Projection
def projection_test():
    # 레코드 추출시 특정 컬럼만 추출할 경우
    # 필요한 필드의 목록을 select() 메소드 내에 선언
    books = Book.select(Book.title, Book.price)

    for book in books:
        print("책 제목 {}: {}원".format(book.title, book.price))


# where과 order by
def where_order_test():
    # 가격이 15000원 이상, 가격이 20000원 미만인 모든 책 목록
    # 가격의 역순
    books = Book.select().where((Book.price >= 15000) & (Book.price < 20000)).order_by(Book.price.desc())
    print("SQL:", books.sql())

    for book in books:
        print("검색된 책:", book)


# ForeignKeyField 타입으로 작성된 컬럼 타입에 relate_name이 설정되어있다면
# PK-FK 기반으로 역참조 가능
def reserve_reference_test():
    # 카테고리 내에 포함된 모든 책 잠조
    categories = Category.select()
    for category in categories:
        print("카테고리:", category)
        # related_name에 설정한 이름으로 역참조 가능
        # print("카테고리 내의 책들:", category.books) # sql문이 나오기 때문에 루프를 돌려야함
        print("카테고리 내의 책들:")
        for book in category.books:
            print(book)



if __name__ == "__main__":
    #create_table_test()
    #insert_relation_test()
    #update_test()
    #delete_test()
    #select_test()
    #projection_test()
    #where_order_test()
    reserve_reference_test()

