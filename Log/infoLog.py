"""
정상 작동시 발생하는 로그를 기록
"""
from Log import debug   #이 객체가 생성이 안되길래 미리 설정
import logging
import logging.handlers
import os
import sys

# 경로 설정
current_dir = os.path.dirname(os.path.realpath(__file__))
FILENAME = 'Log/info/info'

# 로그 저장할 폴더 생성
log_dir = '{}/info'.format(current_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 로거 생성
logger = logging.getLogger('log.info')  # 로거 이름: log.info
logger.setLevel(logging.INFO)  # 로깅 수준: INFO

# 핸들러 생성
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename=FILENAME, when='midnight', interval=1, encoding='utf-8')
file_handler.suffix = '%Y-%m-%d_%H-%M'  # 로그 파일명 날짜 기록 부분 포맷 지정

stream_handler = logging.StreamHandler(stream=sys.stdout)

# 포맷 지정
formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s')
file_handler.setFormatter(formatter)  # 핸들러에 로깅 포맷 할당
stream_handler.setFormatter(formatter)  # 핸들러에 로깅 포맷 할당

# 핸들러 추가
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def getLogger():
    return logger

