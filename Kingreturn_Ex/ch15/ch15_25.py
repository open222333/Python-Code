# 時間資訊asctime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s')  # 等級是DEBUG
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')
