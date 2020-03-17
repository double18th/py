# __init__.py
# 해당 디렉토리를 패키지로 인식하게 하는 파일
# 패키지 import 시 초기화를 담당
from .database import *
__all__ = ['Database']  # 필요한 객체만 공개하고자 할 경우
# import *
