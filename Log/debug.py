"""
디버그용 로그 기록
"""

import logging
import logging.handlers
import os

# 경로 설정
current_dir = os.path.dirname(os.path.realpath(__file__))
FILENAME = 'Log/debugs/debug'

# 로그 저장할 폴더 생성
log_dir = '{}/debugs'.format(current_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 로거 생성
logger = logging.getLogger('log')  # 로거 이름: log
logger.setLevel(logging.DEBUG)  # 로깅 수준: DEBUG

# 핸들러 생성
handler = logging.handlers.TimedRotatingFileHandler(
    filename=FILENAME, when='midnight', interval=1, encoding='utf-8')
handler.suffix = '%Y-%m-%d_%H-%M'  # 로그 파일명 날짜 기록 부분 포맷 지정

# 포맷 지정
formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(message)s')
handler.setFormatter(formatter)  # 핸들러에 로깅 포맷 할당

# 핸들러 추가
logger.addHandler(handler)


def getLogger():
    return logger

