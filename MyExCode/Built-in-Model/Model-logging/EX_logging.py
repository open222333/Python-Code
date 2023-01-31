import logging
import os
import colorlog
from logging.handlers import RotatingFileHandler
from datetime import datetime

'''https://www.cnblogs.com/xyztank/articles/13599165.html'''

cur_path = os.path.dirname(os.path.realpath(__file__))  # 當前項目路徑
log_path = os.path.join(os.path.dirname(cur_path), 'logs')  # log_path為存放日誌的路徑
if not os.path.exists(log_path): os.mkdir(log_path)  # 若不存在logs文件夾，則自動創建

log_colors_config = {
    # 終端輸出日誌顏色配置
    'DEBUG': 'white',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

default_formats = {
    # 終端輸出格式
    'color_format': '%(log_color)s%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s',
    # 日誌輸出格式
    'log_format': '%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s'
}


class HandleLog:
    """
    先創建日誌記錄器（logging.getLogger），然後再設置日誌級別（logger.setLevel），
    接著再創建日誌文件，也就是日誌保存的地方（logging.FileHandler），然後再設置日誌格式（logging.Formatter），
    最後再將日誌處理程序記錄到記錄器（addHandler）
    """

    def __init__(self):
        # 當前日期格式化
        self.__now_time = datetime.now().strftime('%Y-%m-%d')
        # 收集所有日誌信息文件
        self.__all_log_path = os.path.join(log_path, self.__now_time + "-all" + ".log")
        # 收集錯誤日誌信息文件
        self.__error_log_path = os.path.join(log_path, self.__now_time + "-error" + ".log")
        # 創建日誌記錄器
        self.__logger = logging.getLogger()
        # 設置默認日誌記錄器記錄級別
        self.__logger.setLevel(logging.DEBUG)

    @staticmethod
    def __init_logger_handler(log_path):
        """創建日誌記錄器handler，用於收集日誌

        Args:
            log_path (_type_): 日誌文件路徑

        Returns:
            _type_: 日誌記錄器
        """
        # 寫入文件，如果文件超過1M大小時，切割日誌文件，僅保留3個文件
        logger_handler = RotatingFileHandler(filename=log_path, maxBytes=1 * 1024 * 1024, backupCount=3, encoding='utf-8')
        return logger_handler

    @staticmethod
    def __init_console_handle():
        """創建終端日誌記錄器handler，用於輸出到控制台

        Returns:
            _type_: _description_
        """
        console_handle = colorlog.StreamHandler()
        return console_handle

    def __set_log_handler(self, logger_handler, level=logging.DEBUG):
        """設置handler級別並添加到logger收集器

        Args:
            logger_handler (_type_): 日誌記錄器
            level (_type_, optional): 日誌記錄器級別. Defaults to logging.DEBUG.
        """
        logger_handler.setLevel(level=level)
        self.__logger.addHandler(logger_handler)

    def __set_color_handle(self, console_handle):
        """
        设置handler级别并添加到终端logger收集器
        :param console_handle: 终端日志记录器
        :param level: 日志记录器级别
        """
        console_handle.setLevel(logging.DEBUG)
        self.__logger.addHandler(console_handle)

    @staticmethod
    def __set_color_formatter(console_handle, color_config):
        """設置輸出格式-控制台

        Args:
            console_handle (_type_): 終端日誌記錄器
            color_config (_type_): 控制台訊息顏色配置信息
        """
        formatter = colorlog.ColoredFormatter(default_formats["color_format"], log_colors=color_config)
        console_handle.setFormatter(formatter)

    @staticmethod
    def __set_log_formatter(file_handler):
        """設置日誌輸出格式-日誌文件

        Args:
            file_handler (_type_): 日誌記錄器
        """
        formatter = logging.Formatter(default_formats["log_format"], datefmt='%a, %d %b %Y %H:%M:%S')
        file_handler.setFormatter(formatter)

    @staticmethod
    def __close_handler(file_handler):
        """關閉handler

        Args:
            file_handler (_type_): _description_
        """
        file_handler.close()

    def __console(self, level, message):
        """_summary_

        Args:
            level (_type_): _description_
            message (_type_): _description_
        """

        # 創建日誌文件
        all_logger_handler = self.__init_logger_handler(self.__all_log_path)
        error_logger_handler = self.__init_logger_handler(self.__error_log_path)
        console_handle = self.__init_console_handle()

        # 設置日誌格式
        self.__set_log_formatter(all_logger_handler)
        self.__set_log_formatter(error_logger_handler)
        self.__set_color_formatter(console_handle, log_colors_config)

        # 設置handler級別並添加到logger收集器
        self.__set_log_handler(all_logger_handler)
        self.__set_log_handler(error_logger_handler, level=logging.ERROR)
        self.__set_color_handle(console_handle)

        if level == 'info':
            self.__logger.info(message)
        elif level == 'debug':
            self.__logger.debug(message)
        elif level == 'warning':
            self.__logger.warning(message)
        elif level == 'error':
            self.__logger.error(message)
        elif level == 'critical':
            self.__logger.critical(message)

        # 避免日誌輸出重複問題
        self.__logger.removeHandler(all_logger_handler)
        self.__logger.removeHandler(error_logger_handler)
        self.__logger.removeHandler(console_handle)

        # 關閉handler
        self.__close_handler(all_logger_handler)
        self.__close_handler(error_logger_handler)

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    def critical(self, message):
        self.__console('critical', message)


log = HandleLog()

if __name__ == '__main__':
    for i in range(50000):
        log.info("info")
        log.debug("debug")
        log.warning("warning")
        log.error("error")
        log.critical("critical")
