import sqlite3

class Database:
    # 생성자 : __init__
    def __init__(self, db = None):
        # 객체 내부에서 사용할 conn, cursor 객체를 초기화
        self.conn = None
        self.cursor = None

        # db 정보가 인자로 넘어올 경우 open 수행
        if db:
            self.open(db)

    def open(self, db):  # 커넥션 생성
        # 예외 처리
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Database 접속 실패")

    def close(self):  # 접속 해제 메소드
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    # with 문과 함께 사용되는 라이프 사이클 메소드
    # __enter__, __exit__
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with 블록이 끝날 때 호출
        # 커넥션 닫기
        self.close()

    # SELECT 수행용 메소드
    def execute_select(self, sql, parameter = None):
        if parameter is not None:
            self.cursor.execute(sql, parameter)
        else:  # 파라미터가 없다
            self.cursor.execute(sql)

        data = list(self.cursor.fetchall())
        return data

    # INSERT, UPDATE, DATE 수행용 메소드
    def execute_cud(self, sql, parameter = None):
        if parameter is not None:
            self.cursor.execute(sql, parameter)
        else:
            self.cursor.execute(sql)

