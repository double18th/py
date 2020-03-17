# SQLite : 내장 파일 데이터베이스 시스템
import sqlite3  # spqlite 모듈 임포트
import os
from sqlite3 import Error  # Error 객체 임포ㅡ

# 접속 테스트
def create_connection(db_file):
    # 인자에서 넘겨받은 db_file로 데이터베이스 접속
    # 없을 경우 자동으로 생성
    if not os.path.exists("./database"):
        os.makedirs("./database")

    # 접속 수행 - 오류 가능성 있으니 예외처리
    try:
        conn = sqlite3.connect(db_file)
        print("Sqlite3 Version:", sqlite3.version)
    except Error as e:
        print(e)
        print("데이터베이스 접속 오류")
        return None

    print("Connection:", conn)
    return conn  # 접속 객체를 반환


# 테이블 생성
def create_table_test(db_file):
    # 커넥션 생성
    conn = create_connection(db_file)
    # 커서 생성
    cursor = conn.cursor()
    dml = """
    create table if not exists customer (
        id integer primary key autoincrement,
        name varchar(20),
        category integer,
        region varchar(10))        
    """
    # 쿼리 수행
    cursor.execute(dml)
    # 커넥션 종료
    conn.close()


# INSERT
def insert_data_test(db_file, name, category, region):
    conn = create_connection(db_file)
    cursor = conn.cursor()

    # 익명 파라미터 방식 바인딩 : ? (Place Holder)
    # sql = """insert into customer (name, category, region)
    # values(?, ?, ?)
    # """

    # 쿼리 수행 : 데이터는 튜플로 연결
    # res = conn.execute(sql, (name, category, region))

    # Named Parameter 명명 파라미터 방식 바인딩 : dict로 연결
    sql = """
    insert into customer (name, category, region)
    values(:name, :category, :region)
    """
    params = {"name": name,
              "category": category,
              "region": region}
    # 쿼리 수행 : dict 연결
    res = conn.execute(sql, params)


    print("{}개의 행이 영향을 받았습니다.".format(res.rowcount))
    conn.commit()  # INSERT 결과 반영을 위해 commit
    conn.close()


# DELETE 커리 수행
def delete_all_test(db_file):
    # 전체 데이터를 삭제
    conn = create_connection(db_file)
    sql = "delete from customer"
    cursor = conn.execute(sql)

    print("{} 개의 행이 삭제되었습니다".format(cursor.rowcount))
    conn.commit()  # 트랜잭션 반영을 위해 commit()
    # 취소시는 rollback()
    conn.close()

# 데이터 INSERT
def insert_bulk_data(db_file):
    delete_all_test(db_file)
    insert_data_test(db_file, "둘리", 1, "부천")
    insert_data_test(db_file, "장슬기", 2, "인천")
    insert_data_test(db_file, "전가을", 3, "화천")
    insert_data_test(db_file, "기성용", 4, "뉴캐슬")


# 데이터 SELECT
def select_data_test(db_file):
    conn = create_connection(db_file)
    sql = "SELECT * FROM customer"
    cursor = conn.execute(sql)

    print(type(cursor))
    # print(list(cursor))

    # 커서로부터 한개의 레코드를 추출 : fetchone()
    # 커서로부터 여러개의 레코드를 추출 : fetchmany()
    # 커서로부터 전체 레코드를 추출 : fetchall()
    print("fetchone:", cursor.fetchone())
    print("fetchmany:", cursor.fetchmany(3))  # 개수 지정
    res = cursor.fetchall()
    print("fetchall_1:", res)  # print("fetchall_2:", cursor.fetchall())
    conn.close()

# Data Search : WHERE 절
def search_data_test(db_file, region = "인천", category = 2):
    conn = create_connection(db_file)
    # Name Parameter 방식
    sql = """
    SELECT name, region, category
    FROM customer
    WHERE region = :region OR Category = :category
    """

    cursor = conn.execute(sql, {
        "region": region,
        "category": category
    })

    for customer in cursor.fetchall():
        print(customer)


# 사용자 정의 Database 클래스 import
# from mysqlite.database import Database
from mysqlite import *  # __init__.py 내에 선언이 되어있어야함

def mysqlite_class_test(db_file):
    mydb = Database(db_file)
    #sql = "SELECT * FROM customer WHERE region=:region"
    #params = {"region":"인천"}

    #res = mydb.execute_select(sql, params)
    sql = "SELECT * FROM customer"
    res = mydb.execute_select(sql)

    for customer in res:
        print(customer)


if __name__ == "__main__":
    db_file = "./database/mysqlite.db"
    #create_connection(db_file)
    #create_table_test(db_file)
    #insert_data_test(db_file, "둘리", 2, "부천")
    #delete_all_test(db_file)
    #insert_bulk_data(db_file)
    #select_data_test(db_file)
    #search_data_test(db_file)  # 기본값 사용할 것
    #search_data_test(db_file, region="화천")  # region 기본값 사용하지 않음
    mysqlite_class_test(db_file)
