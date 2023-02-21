from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
from datetime import datetime
import logging
import os


class Log():

    def __init__(self, log_name: str) -> None:
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.WARNING)

        self.log_path = 'logs'
        self.log_file = os.path.join(self.log_path, f'{log_name}-all.log')
        self.formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

        # 當前日期
        self.now_time = datetime.now().__format__('%Y-%m-%d')

    def set_log_file_name(self, name: str):
        """設置log檔名稱 預設為 {log_name}-all.log

        Args:
            name (str): _description_
        """
        self.log_file = os.path.join(self.log_path, name)

    def set_date_handler(self, days: int = 7) -> TimedRotatingFileHandler:
        """設置每日log檔

        Args:
            log_file (_type_): log檔名
            days (int, optional): 保留天數. Defaults to 7.

        Returns:
            TimedRotatingFileHandler: _description_
        """
        handler = TimedRotatingFileHandler(self.log_file, when='D', backupCount=days)
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def set_file_handler(self, size: int = 1 * 1024 * 1024, file_amount: int = 5) -> RotatingFileHandler:
        """設置log檔案大小限制

        Args:
            log_file (_type_): log檔名
            size (int, optional): 檔案大小. Defaults to 1*1024*1024 (1M).
            file_amount (int, optional): 檔案數量. Defaults to 5.

        Returns:
            RotatingFileHandler: _description_
        """
        handler = RotatingFileHandler(self.log_file, maxBytes=size, backupCount=file_amount)
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def set_msg_handler(self) -> logging.StreamHandler:
        """設置log steam

        Returns:
            logging.StreamHandler: _description_Ｆ
        """
        handler = logging.StreamHandler()
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    def set_log_formatter(self, formatter: str):
        """設置log格式 formatter

        %(asctime)s - %(name)s - %(levelname)s - %(message)s

        Args:
            formatter (str): log格式.
        """
        self.formatter = formatter

    def set_level(self, level: str = 'WARNING'):
        """設置log等級

        Args:
            level (str): 設定紀錄log等級 DEBUG,INFO,WARNING,ERROR,CRITICAL 預設WARNING
        """
        if level == 'DEBUG':
            self.logger.setLevel(logging.DEBUG)
        elif level == 'INFO':
            self.logger.setLevel(logging.INFO)
        elif level == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        elif level == 'ERROR':
            self.logger.setLevel(logging.ERROR)
        elif level == 'CRITICAL':
            self.logger.setLevel(logging.CRITICAL)

    def debug(self, message: str, exc_info: bool = False):
        self.logger.debug(message, exc_info=exc_info)

    def info(self, message: str, exc_info: bool = False):
        self.logger.info(message, exc_info=exc_info)

    def warning(self, message: str, exc_info: bool = False):
        self.logger.warning(message, exc_info=exc_info)

    def error(self, message: str, exc_info: bool = False):
        self.logger.error(message, exc_info=exc_info)

    def critical(self, message: str, exc_info: bool = False):
        self.logger.critical(message, exc_info=exc_info)
