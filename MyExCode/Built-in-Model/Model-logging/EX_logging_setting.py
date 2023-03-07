from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from traceback import print_exc
from datetime import datetime
import logging
import socket
import os


"""沒有使用 Log Class 的設定範例

; ******log設定******
; 關閉log功能 輸入選項 (true, True, 1) 預設 不關閉
; LOG_DISABLE=1

; logs路徑 預設 logs
; LOG_PATH=

; 關閉紀錄log檔案 輸入選項 (true, True, 1)  預設 不關閉
; LOG_FILE_DISABLE=1

; 設定紀錄log等級 DEBUG,INFO,WARNING,ERROR,CRITICAL 預設WARNING
; LOG_LEVEL=

; 指定log大小(輸入數字) 單位byte, 與 LOG_DAYS 只能輸入一項 若都輸入 LOG_SIZE優先
; LOG_SIZE=

; 指定保留log天數(輸入數字) 預設7
; LOG_DAYS=
"""


try:
    HOSTNAME = socket.gethostname()

    LOG_PATH = os.environ.get('LOG_PATH', 'logs')

    # 關閉log
    LOG_DISABLE = os.environ.get('LOG_DISABLE', False)
    if LOG_DISABLE == 'true' or LOG_DISABLE == 'True' or LOG_DISABLE == '1':
        LOG_DISABLE = True

    # 關閉記錄檔案
    LOG_FILE_DISABLE = os.environ.get('LOG_FILE_DISABLE', False)
    if LOG_FILE_DISABLE == 'true' or LOG_FILE_DISABLE == 'True' or LOG_FILE_DISABLE == '1':
        LOG_FILE_DISABLE = True

    # 設定紀錄log等級 預設WARNING, DEBUG,INFO,WARNING,ERROR,CRITICAL
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING')

    # 指定log大小(輸入數字) 單位byte
    LOG_SIZE = int(os.environ.get('LOG_SIZE', 0))
    # 指定保留log天數(輸入數字) 預設7
    LOG_DAYS = int(os.environ.get('LOG_DAYS', 7))

    log_setting = {
        'LOG_PATH': LOG_PATH,
        'LOG_DISABLE': LOG_DISABLE,
        'LOG_FILE_DISABLE': LOG_FILE_DISABLE,
        'LOG_LEVEL': LOG_LEVEL,
        'LOG_SIZE': LOG_SIZE,
        'LOG_DAYS': LOG_DAYS
    }
except Exception as err:
    print_exc()

# 建立log資料夾
if not os.path.exists(LOG_PATH) and not LOG_DISABLE:
    os.makedirs(LOG_PATH)

if LOG_DISABLE:
    logging.disable()
else:
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    if LOG_SIZE:
        log_file = f'{LOG_PATH}/{HOSTNAME}-mega.log'
        if not LOG_FILE_DISABLE:
            log_file_handler = RotatingFileHandler(f'logs/{log_file}.log', maxBytes=LOG_SIZE, backupCount=5)
            log_file_handler.setFormatter(log_formatter)
    else:
        log_file = f'{LOG_PATH}/{datetime.now().__format__("%Y%m%d")}-{HOSTNAME}.log'
        if not LOG_FILE_DISABLE:
            log_file_handler = TimedRotatingFileHandler(log_file, when='D', backupCount=LOG_DAYS)
            log_file_handler.setFormatter(log_formatter)

    log_msg_handler = logging.StreamHandler()
    log_msg_handler.setFormatter(log_formatter)

    logger = logging.getLogger(HOSTNAME)

    if LOG_LEVEL == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    elif LOG_LEVEL == 'INFO':
        logger.setLevel(logging.INFO)
    elif LOG_LEVEL == 'WARNING':
        logger.setLevel(logging.WARNING)
    elif LOG_LEVEL == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif LOG_LEVEL == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)

    if not LOG_FILE_DISABLE:
        logger.addHandler(log_file_handler)
    logger.addHandler(log_msg_handler)

    logger.debug(log_setting)
