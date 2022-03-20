# 程式日誌模組logging format
import logging

logging.basicConfig(level=logging.DEBUG,format='')  # 等級是DEBUG
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')
