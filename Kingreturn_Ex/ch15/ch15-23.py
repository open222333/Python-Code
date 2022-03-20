# 程式日誌模組logging
import logging

logging.basicConfig(level=logging.WARNING)  # 等級是WARNING
logging.debug('logging message, DEBUG')
logging.info('logging message, INFO')
logging.warning('logging message, WARNING')
logging.error('logging message, ERROR')
logging.critical('logging message, CRITICAL')
