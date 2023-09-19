name = 'byeongheon'
age = 10

def hello():
	return 'hello world'

import logging

# logging.basicConfig(level=logging.DEBUG) # 어느 레벨부터 로깅할지, 기본으로 warning 부터 합니다.
# logging.basicConfig(level=logging.CRITICAL) 
logging.basicConfig(level=logging.CRITICAL, format=f'%(asctime)s - %(message)s')

logging.debug("This is a debug message") # 고쳐야 할 코드, 기록 필요
logging.info("This is an info message") # 정보성 메시지
logging.warning("This is a warning message") # 경고 메시지
logging.error("This is an error message") # 애러 메시지(프로그램은 동작)
logging.critical("This is a critical message") # 프로그램 중지(애러처리 안된경우)