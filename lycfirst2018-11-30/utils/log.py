import os,logging
from logging.handlers import  TimedRotatingFileHandler
from utils.config import LOG_PATH,Config


class Logger(object):
    def __init__(self,logger_name = 'frameword'):
        self.logger = logging.getLogger(logger_name)  #定义long名称
        logging.root.setLevel(logging.DEBUG)  #定义log等级
        # self.log_file_name = 'test.log' #保存log的文件名
        # self.backup_count = 5 #日志输出层级
        # #日志级别
        # self.console_output_level = 'WARNING'
        # self.file_output_level = 'DEBUG'
        # self.formatter =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # #日志输出的格式

        c = Config().get('log')

        self.log_file_name = c.get('file_name')
        self.backup_count = c.get('backup')
        self.console_output_level = c.get('console_level')
        self.file_output_level = c.get('file_level')
        pattern = c.get('pattern')
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
#console 控制台   handler 日志处理器
        if not self.logger.handlers:  #避免重复打印
            console_handler = logging.StreamHandler() # 将错误信息保存到console_handler中
            console_handler.setFormatter(self.formatter)  #设置处理器的输出格式
            console_handler.setLevel(self.console_output_level) #设置处理器的输出等级格式
            self.logger.addHandler(console_handler) #新增一个处理器

            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH,self.log_file_name),
                                                    when = 'D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8')
 # 文件名
 #day  天  字符定义
#一次 等待一天自动重建文件
#5次  保留日志个数  最大保留5个 删除之前的 新增一个删一个
#真
#转码
            file_handler.setFormatter(self.formatter) #定义文件格式
            file_handler.setLevel(self.file_output_level) #定义文件输出等级
            self.logger.addHandler(file_handler) #创建处理器
        return  self.logger

logger = Logger().get_logger()

